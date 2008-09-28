#
Summary:	Gromit - GRaphics Over MIscellaneous Things
Summary(pl.UTF-8):	Gromit - narzędzie do rysowania po ekranie
Name:		gromit
Version:	20041213
Release:	0.1
License:	GPL v2
Group:		Applications
Source0:	http://www.home.unix-ag.org/simon/gromit/%{name}-%{version}.tar.gz
# Source0-md5:	86fd67cfe62b1b955ddcd821e14a8c14
URL:		http://www.home.unix-ag.org/simon/gromit/
BuildRequires:	gtk+2-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Gromit (GRaphics Over MIscellaneous Things) is a small tool to make
annotations on the screen.

%description -l pl.UTF-8
Gromit (Graphics Over MIscellaneous Things) jest prostym, małym narzędziem do
robienia notatek i rysunków bezpośrednio na ekranie.

%prep
%setup -q

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_bindir}
install gromit $RPM_BUILD_ROOT%{_bindir}/gromit

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_bindir}/gromit
