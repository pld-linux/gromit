#
Summary:	Gromit
Summary(pl.UTF-8):	Gromit
Name:		gromit
Version:	20041213
Release:	0.1
License:	- (enter GPL/GPL v2/GPL v3/LGPL/BSD/BSD-like/other license name here)
Group:		Applications
Source0:	http://www.home.unix-ag.org/simon/gromit/%{name}-%{version}.tar.gz
# Source0-md5:	86fd67cfe62b1b955ddcd821e14a8c14
URL:		http://www.home.unix-ag.org/simon/gromit/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Gromit

%description -l pl.UTF-8
Gromit

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
