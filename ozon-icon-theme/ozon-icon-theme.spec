%global theme	Ozon

Name:		ozon-icon-theme
Version:	0.3
Release:	1%{?dist}
Summary:	Default icon theme for OzonOS.
Group:		User Interface/Desktops

License:	GPL-3
URL:		https://github.com/ozonos/ozon-icon-theme
Source0:	%{name}-%{version}.tar.gz

BuildArch:  noarch

%description
 %{theme} is the official icon theme for Ozon OS.


%prep
%setup -q


%install
%make_install


%files
%defattr(-,root,root)
%{_datadir}/icons/%{theme}

%changelog
* Sat Jan 10 2015 Markus S. <kamikazow@web.de>
- BuildArch: noarch
- SPDX License Identifier
- Use variables for source file name

* Sat Dec 20 2014 Paolo Rotolo <paolorotolo@ubuntu.com> - 0.1.0-1
- Initial package for Fedora
