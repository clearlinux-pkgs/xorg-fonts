Name     : xorg-fonts
Version  : 1
Release  : 2
URL      : https://www.x.org/releases/individual/font
Source0  : https://www.x.org/releases/individual/font/encodings-1.0.4.tar.bz2
Source1  : https://www.x.org/releases/individual/font/font-adobe-100dpi-1.0.3.tar.bz2
Source2  : https://www.x.org/releases/individual/font/font-adobe-75dpi-1.0.3.tar.bz2
Source3  : https://www.x.org/releases/individual/font/font-adobe-utopia-100dpi-1.0.4.tar.bz2
Source4  : https://www.x.org/releases/individual/font/font-adobe-utopia-75dpi-1.0.4.tar.bz2
Source5  : https://www.x.org/releases/individual/font/font-adobe-utopia-type1-1.0.4.tar.bz2
Source6  : https://www.x.org/releases/individual/font/font-arabic-misc-1.0.3.tar.bz2
Source7  : https://www.x.org/releases/individual/font/font-bh-100dpi-1.0.3.tar.bz2
Source8  : https://www.x.org/releases/individual/font/font-bh-75dpi-1.0.3.tar.bz2
Source9  : https://www.x.org/releases/individual/font/font-bh-lucidatypewriter-100dpi-1.0.3.tar.bz2
Source10  : https://www.x.org/releases/individual/font/font-bh-lucidatypewriter-75dpi-1.0.3.tar.bz2
#Source11  : https://www.x.org/releases/individual/font/font-bh-ttf-1.0.3.tar.bz2
Source12  : https://www.x.org/releases/individual/font/font-bh-type1-1.0.3.tar.bz2
Source13  : https://www.x.org/releases/individual/font/font-bitstream-100dpi-1.0.3.tar.bz2
Source14  : https://www.x.org/releases/individual/font/font-bitstream-75dpi-1.0.3.tar.bz2
Source15  : https://www.x.org/releases/individual/font/font-bitstream-speedo-1.0.2.tar.bz2
Source16  : https://www.x.org/releases/individual/font/font-bitstream-type1-1.0.3.tar.bz2
Source17  : https://www.x.org/releases/individual/font/font-cronyx-cyrillic-1.0.3.tar.bz2
Source18  : https://www.x.org/releases/individual/font/font-cursor-misc-1.0.3.tar.bz2
Source19  : https://www.x.org/releases/individual/font/font-daewoo-misc-1.0.3.tar.bz2
Source20  : https://www.x.org/releases/individual/font/font-dec-misc-1.0.3.tar.bz2
Source21  : https://www.x.org/releases/individual/font/font-ibm-type1-1.0.3.tar.bz2
Source22  : https://www.x.org/releases/individual/font/font-isas-misc-1.0.3.tar.bz2
Source23  : https://www.x.org/releases/individual/font/font-jis-misc-1.0.3.tar.bz2
Source24  : https://www.x.org/releases/individual/font/font-micro-misc-1.0.3.tar.bz2
Source25  : https://www.x.org/releases/individual/font/font-misc-cyrillic-1.0.3.tar.bz2
Source26  : https://www.x.org/releases/individual/font/font-misc-ethiopic-1.0.3.tar.bz2
Source27  : https://www.x.org/releases/individual/font/font-misc-meltho-1.0.3.tar.bz2
Source28  : https://www.x.org/releases/individual/font/font-misc-misc-1.1.2.tar.bz2
Source29  : https://www.x.org/releases/individual/font/font-mutt-misc-1.0.3.tar.bz2
Source30  : https://www.x.org/releases/individual/font/font-schumacher-misc-1.1.2.tar.bz2
Source31  : https://www.x.org/releases/individual/font/font-screen-cyrillic-1.0.4.tar.bz2
Source32  : https://www.x.org/releases/individual/font/font-sony-misc-1.0.3.tar.bz2
Source33  : https://www.x.org/releases/individual/font/font-sun-misc-1.0.3.tar.bz2
Source34  : https://www.x.org/releases/individual/font/font-winitzki-cyrillic-1.0.3.tar.bz2
Source35  : https://www.x.org/releases/individual/font/font-xfree86-type1-1.0.4.tar.bz2
Summary  : X.org fonts
Group    : Development/Tools
License  : X11 MIT NTP HPND Public-Domain
Requires: xorg-fonts-data = %{version}-%{release}
Requires: xorg-fonts-license = %{version}-%{release}
BuildRequires : mkfontscale-bin
BuildRequires : pkgconfig(fontutil)
BuildRequires : pkgconfig(xorg-macros)
BuildRequires : mkfontdir
BuildRequires : bdftopcf

%description
Collection of X.org fonts

%package data
Summary: data components for the xorg-fonts package.
Group: Data

%description data
data components for the xorg-fonts package.


%package license
Summary: license components for the xorg-fonts package.
Group: Default

%description license
license components for the xorg-fonts package.


%prep
%setup -q -n encodings-1.0.4 -b 0
%setup -q -n font-adobe-100dpi-1.0.3 -b 1
%setup -q -n font-adobe-75dpi-1.0.3 -b 2
%setup -q -n font-adobe-utopia-100dpi-1.0.4 -b 3
%setup -q -n font-adobe-utopia-75dpi-1.0.4 -b 4
%setup -q -n font-adobe-utopia-type1-1.0.4 -b 5
%setup -q -n font-arabic-misc-1.0.3 -b 6
%setup -q -n font-bh-100dpi-1.0.3 -b 7
%setup -q -n font-bh-75dpi-1.0.3 -b 8
%setup -q -n font-bh-lucidatypewriter-100dpi-1.0.3 -b 9
%setup -q -n font-bh-lucidatypewriter-75dpi-1.0.3 -b 10
#%setup -q -n font-bh-ttf-1.0.3 -b 11
%setup -q -n font-bh-type1-1.0.3 -b 12
%setup -q -n font-bitstream-100dpi-1.0.3 -b 13
%setup -q -n font-bitstream-75dpi-1.0.3 -b 14
%setup -q -n font-bitstream-speedo-1.0.2 -b 15
%setup -q -n font-bitstream-type1-1.0.3 -b 16
%setup -q -n font-cronyx-cyrillic-1.0.3 -b 17
%setup -q -n font-cursor-misc-1.0.3 -b 18
%setup -q -n font-daewoo-misc-1.0.3 -b 19
%setup -q -n font-dec-misc-1.0.3 -b 20
%setup -q -n font-ibm-type1-1.0.3 -b 21
%setup -q -n font-isas-misc-1.0.3 -b 22
%setup -q -n font-jis-misc-1.0.3 -b 23
%setup -q -n font-micro-misc-1.0.3 -b 24
%setup -q -n font-misc-cyrillic-1.0.3 -b 25
%setup -q -n font-misc-ethiopic-1.0.3 -b 26
%setup -q -n font-misc-meltho-1.0.3 -b 27
%setup -q -n font-misc-misc-1.1.2 -b 28
%setup -q -n font-mutt-misc-1.0.3 -b 29
%setup -q -n font-schumacher-misc-1.1.2 -b 30
%setup -q -n font-screen-cyrillic-1.0.4 -b 31
%setup -q -n font-sony-misc-1.0.3 -b 32
%setup -q -n font-sun-misc-1.0.3 -b 33
%setup -q -n font-winitzki-cyrillic-1.0.3 -b 34
%setup -q -n font-xfree86-type1-1.0.4 -b 35

%build
cd ../encodings-1.0.4
%configure
cd ../font-adobe-100dpi-1.0.3
%configure
cd ../font-adobe-75dpi-1.0.3
%configure
cd ../font-adobe-utopia-100dpi-1.0.4
%configure
cd ../font-adobe-utopia-75dpi-1.0.4
%configure
cd ../font-adobe-utopia-type1-1.0.4
%configure
cd ../font-arabic-misc-1.0.3
%configure
cd ../font-bh-100dpi-1.0.3
%configure
cd ../font-bh-75dpi-1.0.3
%configure
cd ../font-bh-lucidatypewriter-100dpi-1.0.3
%configure
cd ../font-bh-lucidatypewriter-75dpi-1.0.3
%configure
#cd ../font-bh-ttf-1.0.3
#%configure
cd ../font-bh-type1-1.0.3
%configure
cd ../font-bitstream-100dpi-1.0.3
%configure
cd ../font-bitstream-75dpi-1.0.3
%configure
cd ../font-bitstream-speedo-1.0.2
%configure
cd ../font-bitstream-type1-1.0.3
%configure
cd ../font-cronyx-cyrillic-1.0.3
%configure
cd ../font-cursor-misc-1.0.3
%configure
cd ../font-daewoo-misc-1.0.3
%configure
cd ../font-dec-misc-1.0.3
%configure
cd ../font-ibm-type1-1.0.3
%configure
cd ../font-isas-misc-1.0.3
%configure
cd ../font-jis-misc-1.0.3
%configure
cd ../font-micro-misc-1.0.3
%configure
cd ../font-misc-cyrillic-1.0.3
%configure
cd ../font-misc-ethiopic-1.0.3
%configure
cd ../font-misc-meltho-1.0.3
%configure
cd ../font-misc-misc-1.1.2
%configure
cd ../font-mutt-misc-1.0.3
%configure
cd ../font-schumacher-misc-1.1.2
%configure
cd ../font-screen-cyrillic-1.0.4
%configure
cd ../font-sony-misc-1.0.3
%configure
cd ../font-sun-misc-1.0.3
%configure
cd ../font-winitzki-cyrillic-1.0.3
%configure
cd ../font-xfree86-type1-1.0.4
%configure

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/xorg-fonts
cd ../encodings-1.0.4
cp COPYING %{buildroot}/usr/share/package-licenses/xorg-fonts/encodings_COPYING
%make_install
cd ../font-adobe-100dpi-1.0.3
cp COPYING %{buildroot}/usr/share/package-licenses/xorg-fonts/font-adobe-100dpi_COPYING
%make_install
cd ../font-adobe-75dpi-1.0.3
cp COPYING %{buildroot}/usr/share/package-licenses/xorg-fonts/font-adobe-75dpi_COPYING
%make_install
cd ../font-adobe-utopia-100dpi-1.0.4
cp COPYING %{buildroot}/usr/share/package-licenses/xorg-fonts/font-adobe-utopia-100dpi_COPYING
%make_install
cd ../font-adobe-utopia-75dpi-1.0.4
cp COPYING %{buildroot}/usr/share/package-licenses/xorg-fonts/font-adobe-utopia-75dpi_COPYING
%make_install
cd ../font-adobe-utopia-type1-1.0.4
cp COPYING %{buildroot}/usr/share/package-licenses/xorg-fonts/font-adobe-utopia-type1_COPYING
%make_install
cd ../font-arabic-misc-1.0.3
cp COPYING %{buildroot}/usr/share/package-licenses/xorg-fonts/font-arabic-misc_COPYING
%make_install
cd ../font-bh-100dpi-1.0.3
cp COPYING %{buildroot}/usr/share/package-licenses/xorg-fonts/font-bh-100dpi_COPYING
%make_install
cd ../font-bh-75dpi-1.0.3
cp COPYING %{buildroot}/usr/share/package-licenses/xorg-fonts/font-bh-75dpi_COPYING
%make_install
cd ../font-bh-lucidatypewriter-100dpi-1.0.3
cp COPYING %{buildroot}/usr/share/package-licenses/xorg-fonts/font-bh-lucidatypewriter-100dpi_COPYING
%make_install
cd ../font-bh-lucidatypewriter-75dpi-1.0.3
cp COPYING %{buildroot}/usr/share/package-licenses/xorg-fonts/font-bh-lucidatypewriter-75dpi_COPYING
%make_install
#cd ../font-bh-ttf-1.0.3
#cp COPYING %{buildroot}/usr/share/package-licenses/xorg-fonts/font-bh-ttf_COPYING
#%make_install
cd ../font-bh-type1-1.0.3
cp COPYING %{buildroot}/usr/share/package-licenses/xorg-fonts/font-bh-type1_COPYING
%make_install
cd ../font-bitstream-100dpi-1.0.3
cp COPYING %{buildroot}/usr/share/package-licenses/xorg-fonts/font-bitstream-100dpi_COPYING
%make_install
cd ../font-bitstream-75dpi-1.0.3
cp COPYING %{buildroot}/usr/share/package-licenses/xorg-fonts/font-bitstream-75dpi_COPYING
%make_install
cd ../font-bitstream-speedo-1.0.2
cp COPYING %{buildroot}/usr/share/package-licenses/xorg-fonts/font-bitstream-speedo_COPYING
%make_install
cd ../font-bitstream-type1-1.0.3
cp COPYING %{buildroot}/usr/share/package-licenses/xorg-fonts/font-bitstream-type1_COPYING
%make_install
cd ../font-cronyx-cyrillic-1.0.3
cp COPYING %{buildroot}/usr/share/package-licenses/xorg-fonts/font-cronyx-cyrillic_COPYING
%make_install
cd ../font-cursor-misc-1.0.3
cp COPYING %{buildroot}/usr/share/package-licenses/xorg-fonts/font-cursor-misc_COPYING
%make_install
cd ../font-daewoo-misc-1.0.3
cp COPYING %{buildroot}/usr/share/package-licenses/xorg-fonts/font-daewoo-misc_COPYING
%make_install
cd ../font-dec-misc-1.0.3
cp COPYING %{buildroot}/usr/share/package-licenses/xorg-fonts/font-dec-misc_COPYING
%make_install
cd ../font-ibm-type1-1.0.3
cp COPYING %{buildroot}/usr/share/package-licenses/xorg-fonts/font-ibm-type1_COPYING
%make_install
cd ../font-isas-misc-1.0.3
cp COPYING %{buildroot}/usr/share/package-licenses/xorg-fonts/font-isas-misc_COPYING
%make_install
cd ../font-jis-misc-1.0.3
cp COPYING %{buildroot}/usr/share/package-licenses/xorg-fonts/font-jis-misc_COPYING
%make_install
cd ../font-micro-misc-1.0.3
cp COPYING %{buildroot}/usr/share/package-licenses/xorg-fonts/font-micro-misc_COPYING
%make_install
cd ../font-misc-cyrillic-1.0.3
cp COPYING %{buildroot}/usr/share/package-licenses/xorg-fonts/font-misc-cyrillic_COPYING
%make_install
cd ../font-misc-ethiopic-1.0.3
cp COPYING %{buildroot}/usr/share/package-licenses/xorg-fonts/font-misc-ethiopic_COPYING
%make_install
cd ../font-misc-meltho-1.0.3
cp COPYING %{buildroot}/usr/share/package-licenses/xorg-fonts/font-misc-meltho_COPYING
%make_install
cd ../font-misc-misc-1.1.2
cp COPYING %{buildroot}/usr/share/package-licenses/xorg-fonts/font-misc-misc_COPYING
%make_install
cd ../font-mutt-misc-1.0.3
cp COPYING %{buildroot}/usr/share/package-licenses/xorg-fonts/font-mutt-misc_COPYING
%make_install
cd ../font-schumacher-misc-1.1.2
cp COPYING %{buildroot}/usr/share/package-licenses/xorg-fonts/font-schumacher-misc_COPYING
%make_install
cd ../font-screen-cyrillic-1.0.4
cp COPYING %{buildroot}/usr/share/package-licenses/xorg-fonts/font-screen-cyrillic_COPYING
%make_install
cd ../font-sony-misc-1.0.3
cp COPYING %{buildroot}/usr/share/package-licenses/xorg-fonts/font-sony-misc_COPYING
%make_install
cd ../font-sun-misc-1.0.3
cp COPYING %{buildroot}/usr/share/package-licenses/xorg-fonts/font-sun-misc_COPYING
%make_install
cd ../font-winitzki-cyrillic-1.0.3
cp COPYING %{buildroot}/usr/share/package-licenses/xorg-fonts/font-winitzki-cyrillic_COPYING
%make_install
cd ../font-xfree86-type1-1.0.4
cp COPYING %{buildroot}/usr/share/package-licenses/xorg-fonts/font-xfree86-type1_COPYING
%make_install

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/fonts/X11

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/xorg-fonts
