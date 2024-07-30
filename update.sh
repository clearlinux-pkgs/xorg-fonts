#!/bin/bash
set -e -o pipefail

PKG=xorg-fonts
RELEASE_URL="https://www.x.org/archive/individual/font/"

errexit() {
	local ret=1
	echo "Error: $1"
	if [[ -n "$2" ]]; then
		ret=2
	fi
	exit $ret
}

echo -n "Pulling package repo changes: "
git pull --ff-only

echo "Retrieving source table from ${RELEASE_URL}"
PACKAGES=($(curl -s "${RELEASE_URL}" | grep -oiE 'href="[a-z][^\"]+\.tar\.(bz2|gz)"' | cut -d = -f 2 | sed 's|"||g' | sort -V))

# Pick best compression format (alphabetical - bz2 > gz > xz) of latest version of encodings package
ver_encodings=$(printf -- "%s\n" "${PACKAGES[@]}" | grep '^encodings-' | tail -1 | sed -E 's#encodings-([0-9\.]+)\.tar.*#\1#')
pkg_encodings=$(printf -- "%s\n" "${PACKAGES[@]}" | grep "^encodings-${ver_encodings}\." | sort | head -1)
echo "$pkg_encodings"

# Update encodings
sed -E -i "s#encodings-[0-9\.]+\.tar\.(bz2|gz|xz)#${pkg_encodings}#" ${PKG}.spec
sed -E -i "s#encodings-[0-9\.]+[0-9]+#${pkg_encodings%%.tar.*}#" ${PKG}.spec

# Get list of font packages by name only
for font in $(printf -- "%s\n" "${PACKAGES[@]}" | grep '^font-' | sed -E 's#-[0-9\.]+\.tar\.(bz2|gz)$##' | sort -u); do
	# Pick best compression format of latest version of each font package
	ver_font=$(printf -- "%s\n" "${PACKAGES[@]}" | grep -P "^${font}-.*\.tar\.(bz2|gz|xz)$" | tail -1 | sed -E "s#${font}-([0-9\.]+)\.tar.*#\1#")
	pkg_font=$(printf -- "%s\n" "${PACKAGES[@]}" | grep -P "^${font}-${ver_font}\." | sort | head -1)
	echo "$pkg_font"
	sed -E -i "s#(${font})-[0-9.]+[0-9]+#\1-${ver_font}#" ${PKG}.spec
	sed -E -i "s#${font}-[0-9.]+\.tar\.(bz2|gz|xz)#${pkg_font}#" ${PKG}.spec
done

# Check whether anything changed.
if ! git status | grep -qE '^\s+modified:\s+'; then
	echo "No changes."
	exit 0
fi

echo "Changes detected. Preparing commit."
make generateupstream
make bumpnogit
git add -u
git commit -m "Update to latest release" -m "$(git diff --cached ${PKG}.spec | grep ^+%setup | grep -oP '(encodings|font)-\S+')"
make koji-nowait
