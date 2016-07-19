Summary:	Semplicy drivers
Name:		semplicy-drivers
Version:	%{fedora}
Release:	1%{?dist}

License:	GPL-3
Group:		System Environment/Base

Requires:	akmod-wl
Requires:	broadcom-wl
Requires:	dkms
Requires:	gcc
Requires:	gcc-c++
Requires:	isight-firmware-tools
Requires:	kernel-headers

BuildArch:	noarch

%description
The hardware drivers for Semplicy Linux.

%files

%changelog
* Tue Jul 19 2016 Egor Mikhailov E. <xeneloid@yandex.ru> - 0.0-1
- Initial package
