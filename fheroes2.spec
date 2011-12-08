%define rev r2693
Name:		fheroes2
Version:	20111109
Release:	%mkrel 1
Summary:	Free implementation of Heroes of the Might and Magic II engine
License:	GPL
Group:		Games/Strategy
Url:		http://sourceforge.net/projects/fheroes2/
Source:		http://sourceforge.net/projects/fheroes2/files/fheroes2/%{name}-src-%{rev}.tgz
Source2:	%{name}.sh
Source3:	%{name}.png
Source4:	%{name}.desktop
Source5:	%{name}.cfg
Patch0:		fheroes2-r2693-zlib.patch
BuildRequires:	gcc-c++
BuildRequires:	SDL_image-devel
BuildRequires:	SDL_mixer-devel
BuildRequires:	SDL_net-devel
BuildRequires:	SDL_ttf-devel
BuildRequires:	freetype-devel
BuildRequires:	png-devel
BuildRequires:	zlib-devel

%description
Free implementation of Heroes of the Might and Magic II engine.
You need to copy files from data and maps directories from original game
into your /usr/share/games/fheroes2/{maps,data} directories respectively

%prep
%setup -qn fheroes-src
%patch0 -p1 -b .zlib

%build
%make WITH_AI=simple CONFIGURE_FHEROES2_DATA="%{_gamesdatadir}/%{name}/"

%install
# let's create directory structure...
%__mkdir_p %{buildroot}%{_gamesbindir}
%__mkdir_p %{buildroot}%{_datadir}/applications
%__mkdir_p %{buildroot}%{_datadir}/pixmaps
%__mkdir_p %{buildroot}%{_gamesdatadir}/%{name}/{data,maps}

# and install what we need where we need it to be...
%__install -pm755 %{name} %{buildroot}%{_gamesbindir}/%{name}.bin
%__install -pm755 %{SOURCE2} %{buildroot}%{_gamesbindir}/%{name}
%__install -pm 644 %{name}.cfg %{buildroot}%{_gamesdatadir}/%{name}/
%__install -pm 644 %{name}.key %{buildroot}%{_gamesdatadir}/%{name}/
%__install -pm 644 %{SOURCE3} %{buildroot}%{_datadir}/pixmaps/%{name}.png
%__install -pm 644 %{SOURCE4} %{buildroot}%{_datadir}/applications/%{name}.desktop
%__install -pm 644 %{SOURCE5} %{buildroot}%{_gamesdatadir}/%{name}/

%files
%defattr(-,root,root)
%doc AUTHORS changelog.txt COPYING LICENSE README
%{_gamesbindir}/*
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/applications/%{name}.desktop
%{_gamesdatadir}/%{name}

