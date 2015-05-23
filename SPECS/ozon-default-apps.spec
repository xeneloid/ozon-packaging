Summary:	Ozon default applications
Name:		ozon-default-apps
Version:	%{fedora}
Release:	2%{?dist}

License:	GPL-3
Group:		System Environment/Base

URL:		http://ozonos.github.io

Requires:	gnome-shell >= 3.14.0
Requires:	gnome-terminal >= 3.14.0
Requires:	gedit >= 3.14.0
Requires:	nautilus >= 3.14.0
Requires:	file-roller >= 3.14.0
Requires:	file-roller-nautilus >= 3.14.0
Requires:	totem >= 3.14.0
Requires:	gnome-disk-utility >= 3.14.0
Requires:	gnome-calculator >= 3.14.0
Requires:	gnome-screenshot >= 3.14.0
Requires:	gnome-software >= 3.14.0
Requires:	gnome-system-monitor >= 3.14.0
Requires:	gnome-tweak-tool >= 3.14.0

Requires:	gthumb
Requires:	chromium
Requires:	tomahawk
Requires:	steam

Requires:	preload
Requires:	libmtp


BuildArch:	noarch

%description
The default applications for Ozon desktop.

%files

%changelog
* Tue Feb 17 2015 Satyajit Sahoo <satya164@fedoraproject.org> - 0.0-1
- Initial package for Fedora

