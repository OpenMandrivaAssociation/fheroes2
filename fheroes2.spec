#define debug_package %{nil}
%define _empty_manifest_terminate_build 0

Name:		fheroes2
Version:	1.0.6
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
BuildRequires:	cmake
BuildRequires:	SDL2_image-devel
BuildRequires:	SDL2_mixer-devel
BuildRequires:	SDL2_net-devel
BuildRequires:	SDL2_ttf-devel
BuildRequires:	freetype-devel
BuildRequires:	png-devel
BuildRequires:	zlib-devel
BuildRequires: glibc-static-devel

%description
Free implementation of Heroes of the Might and Magic II engine.
You need to copy files from data and maps directories from original game
into your /usr/share/games/fheroes2/{maps,data} directories respectively

%prep
%setup -q
%autopatch -p1

%build
%make WITH_SDL2="ON" CXX=%{__cxx}

%install
# let's create directory structure...
%__mkdir_p %{buildroot}%{_gamesbindir}
%__mkdir_p %{buildroot}%{_datadir}/applications
%__mkdir_p %{buildroot}%{_datadir}/pixmaps
%__mkdir_p %{buildroot}%{_gamesdatadir}/%{name}/{data,maps}

# and install what we need where we need it to be...
%__install -pm755 %{name} %{buildroot}%{_gamesbindir}/%{name}.bin
%__install -pm755 %{SOURCE2} %{buildroot}%{_gamesbindir}/%{name}
#__install -pm 644 %{name}.cfg %{buildroot}%{_gamesdatadir}/%{name}/
#__install -pm 644 %{name}.key %{buildroot}%{_gamesdatadir}/%{name}/
%__install -pm 644 %{SOURCE3} %{buildroot}%{_datadir}/pixmaps/%{name}.png
%__install -pm 644 %{SOURCE4} %{buildroot}%{_datadir}/applications/%{name}.desktop
%__install -pm 644 %{SOURCE5} %{buildroot}%{_gamesdatadir}/%{name}/

%files
%doc LICENSE
%{_gamesbindir}/*
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/applications/%{name}.desktop
%{_gamesdatadir}/%{name}
