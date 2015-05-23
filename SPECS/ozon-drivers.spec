Summary:	Ozon drivers
Name:		ozon-drivers
Version:	%{fedora}
Release:	1%{?dist}

License:	GPL-3
Group:		System Environment/Base

URL:		http://ozonos.github.io

Requires:	akmod-wl
Requires:	broadcom-wl
Requires:	dkms
Requires:	gcc
Requires:	gcc-c++
Requires:	isight-firmware-tools
Requires:	kernel-headers

BuildArch:	noarch

%description
The hardware drivers for Ozon desktop.

%files

%changelog
* Sat May 23 2015 Satyajit Sahoo <satya164@fedoraproject.org> - 0.0-1
- Initial package for Fedora
