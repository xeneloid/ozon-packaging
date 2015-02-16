%global theme	Ozon

Name:		ozon-shell-theme
Version:	0.1
Release:	1%{?dist}
Summary:	%{theme} theme for Gnome Shell
Group:		User Interface/Desktops

License:	GPL-3
URL:		http://ozonos.github.io
Source0:	%{name}-%{version}.tar.gz

Requires:	gnome-shell >= 3.12.0

BuildArch:	noarch

%description
%{theme} is the official Gnome Shell theme for Ozon OS.


%prep
%setup -q


%install
%{__install} -d -m755 %{buildroot}%{_datadir}/themes/%{theme}
%{__cp} -pr gnome-shell %{buildroot}%{_datadir}/themes/%{theme}


%files
%defattr(-,root,root)
%doc LICENSE README.md
%{_datadir}/themes/%{theme}


%changelog
* Sat Feb 17 2015 Satyajit Sahoo <satya164@fedoraproject.org> - 0.0-1
- Initial package for Fedora

