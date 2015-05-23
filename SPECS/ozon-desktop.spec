Summary:		Ozon desktop
Name:			ozon-desktop
Version:		21
Release:		1%{?dist}

License:		GPL-3
Group:			System Environment/Base

URL:			http://ozonos.github.io

Requires:		ozon-release = %{version}
Requires:		ozon-default-apps = %{version}
Requires:		ozon-multimedia-codecs = %{version}
Requires:		ozon-font-config = %{version}
Requires:		ozon-backgrounds = %{version}
Requires:		ozon-icon-theme
Requires:		ozon-gtk-theme
Requires:		ozon-shell-theme
Requires:		atom-experience = %{version}

BuildArch:		noarch


%description
The complete Ozon desktop.

%files

%changelog
* Tue Feb 17 2015 Satyajit Sahoo <satya164@fedoraproject.org> - 0.0-1
- Initial package for Fedora

