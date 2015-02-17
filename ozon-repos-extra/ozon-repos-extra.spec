Name:		ozon-repos-extra
Version:	21
Release:	1%{?dist}
Summary:	Extra repositories for Ozon.
Group:		System Environment/Base

License:	GPL-3
URL:		http://ozonos.github.io

BuildArch:  noarch

%description
 Extra repositories used in Ozon OS.


%install
%{__install} -d -m755 %{buildroot}/etc/yum.repos.d
curl http://copr.fedoraproject.org/coprs/spot/chromium/repo/fedora-21/spot-chromium-fedora-%{version}.repo -o %{buildroot}/etc/yum.repos.d/fedora-chromium-stable.repo


%files
%defattr(-,root,root)
/etc/yum.repos.d/fedora-chromium-stable.repo

%changelog
* Tue Feb 17 2015 Satyajit Sahoo <satya164@fedoraproject.org> - 0.0-1
- Initial package for Fedora

