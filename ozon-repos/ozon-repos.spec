Name:		ozon-repos
Version:	21
Release:	2%{?dist}
Summary:	Repositories for Ozon OS.
Group:		System Environment/Base

License:	GPL-3
URL:		http://ozonos.github.io

BuildArch:  noarch

%description
 Default repositories used in Ozon OS.


%install
%{__install} -d -m755 %{buildroot}/etc/yum.repos.d
cat << EOF >>%{buildroot}/etc/yum.repos.d/ozonos.repo
[ozonos]
name=Repository for Ozon OS
baseurl=http://goodies.ozon-os.com/repo/\$releasever/
gpgcheck=0
enabled=1
skip_if_unavailable=1
EOF


%files
%defattr(-,root,root)
/etc/yum.repos.d/ozonos.repo

%changelog
* Tue Feb 17 2015 Satyajit Sahoo <satya164@fedoraproject.org> - 0.0-1
- Initial package for Fedora

