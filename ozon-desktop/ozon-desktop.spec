Summary:        Ozon desktop
Name:           ozon-desktop
Version:        21
Release:        0

License:        GPL-3
Group:          System Environment/Base

URL:            http://ozonos.github.io

Requires:       ozon-release = %{version}
Requires:       ozon-gtk-theme
Requires:       ozon-shell-theme
Requires:       atom-dock
Requires:       atom-launcher
Requires:       atom-panel

BuildArch:      noarch

%description
The complete Ozon desktop.

%files
%defattr(-,root,root,-)

%changelog
* Sat Feb 18 2015 Satyajit Sahoo <satya164@fedoraproject.org> - 0.0-1
- Initial package for Fedora

