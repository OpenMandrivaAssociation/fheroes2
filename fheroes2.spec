#define debug_package %{nil}
%define _empty_manifest_terminate_build 0

Name:		fheroes2
Version:	1.1.6
Release:	1
Epoch:		1
Summary:	Free implementation of Heroes of the Might and Magic II engine
License:	GPL
Group:		Games/Strategy
Url:		https://github.com/inhub
Source0:	https://github.com/ihhub/fheroes2/archive/%{version}/%{name}-%{version}.tar.gz
Source2:	%{name}.sh
Source3:	%{name}.png
Source4:	%{name}.desktop
Source5:	%{name}.cfg
BuildRequires:	gcc-c++
BuildRequires:	gettext
BuildRequires:	cmake
BuildRequires:  pkgconfig(sdl2)
BuildRequires:	pkgconfig(SDL2_image)
BuildRequires:	pkgconfig(SDL2_mixer)
BuildRequires:	pkgconfig(SDL2_net)
BuildRequires:	pkgconfig(SDL2_ttf)
BuildRequires:	pkgconfig(freetype2)
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(zlib)
BuildRequires:  glibc-static-devel
BuildRequires:	locales-extra-charsets

%description
Free implementation of Heroes of the Might and Magic II engine.
You need to copy files from data and maps directories from original game
into your /usr/share/fheroes2/{maps,data} directories respectively

%prep
%setup -q
%autopatch -p1

%build
%cmake
%make_build

%install
%make_install -C build
for i in %{buildroot}%{_datadir}/fheroes2/files/lang/*.mo; do
	echo "%%lang($(basename $i .mo)) $(echo $i |sed -e 's,^.*%{_datadir},%%{_datadir},')" >>fheroes2.lang
done

%files -f fheroes2.lang
%doc %{_datadir}/doc/fheroes2/
%{_bindir}/fheroes2
%{_datadir}/applications/%{name}.desktop
%dir %{_datadir}/fheroes2
%dir %{_datadir}/fheroes2/files
%dir %{_datadir}/fheroes2/files/data
%dir %{_datadir}/fheroes2/files/lang
%{_datadir}/fheroes2/files/data/resurrection.h2d
%{_datadir}/metainfo/fheroes2.metainfo.xml
%{_iconsdir}/hicolor/*x*/apps/fheroes2.png
