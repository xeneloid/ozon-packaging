Name:		atom-panel
Version:	0.1.0
Release:	1%{?dist}
Summary:	Atom panel extension for gnome-shell.
Group:		User Interface/Desktops

License:	GPL-3
URL:		https://github.com/ozonos/atom-panel
Source0:	%{name}-%{version}.tar.gz

Requires:	gnome-shell >= 3.12.0

BuildArch:	noarch

%description
 A custom panel for gnome-shell.


%prep
%setup -q


%install
%make_install


%files
%defattr(-,root,root)
%{_datadir}/gnome-shell/extensions/%{name}@ozonos.org

%changelog
* Thu Nov 28 2014 Paolo Rotolo <paolorotolo@ubuntu.com> - 0.1.0-1
- Initial package for Fedora
