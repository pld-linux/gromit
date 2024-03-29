#
%bcond_without	desktop		# build without .desktop file (and daemon dependency)
#
Summary:	Gromit - GRaphics Over MIscellaneous Things
Summary(pl.UTF-8):	Gromit - narzędzie do rysowania po ekranie
Name:		gromit
Version:	20041213
Release:	1
License:	GPL v2
Group:		X11/Applications/Graphics
Source0:	http://www.home.unix-ag.org/simon/gromit/%{name}-%{version}.tar.gz
# Source0-md5:	86fd67cfe62b1b955ddcd821e14a8c14
Source1:	%{name}.desktop
URL:		http://www.home.unix-ag.org/simon/gromit/
BuildRequires:	gtk+2-devel
%{?with_desktop:Requires:	daemon}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Gromit (GRaphics Over MIscellaneous Things) is a small tool to make
annotations on the screen.

%description -l pl.UTF-8
Gromit (Graphics Over MIscellaneous Things) jest prostym, małym
narzędziem do robienia notatek i rysunków bezpośrednio na ekranie.

%prep
%setup -q

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_bindir},%{_desktopdir}}
install gromit $RPM_BUILD_ROOT%{_bindir}/gromit
%{?with_desktop:install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_bindir}/gromit
%{?with_desktop:%{_desktopdir}/gromit.desktop}
