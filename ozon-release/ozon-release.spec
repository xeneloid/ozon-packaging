%define codename Hydrogen

Summary:        Ozon release files
Name:           ozon-release
Version:        21
Release:        2%{?dist}
License:        MIT
Group:          System Environment/Base

URL:            http://ozonos.github.io
Source:         %{name}-%{version}.tar.gz
Requires:       fedora-release = %{version}

BuildArch:      noarch

%description
Ozon release files and default settings.


%prep
%setup -q

%build


%install
%{__install} -d -m755 %{buildroot}/etc
echo "Ozon release %{version} (%{codename})" > %{buildroot}/etc/ozon-release
%{__install} -d -m755 %{buildroot}%{_datadir}/glib-2.0/schemas/
%{__install} -m 0644 org.ozonos.gschema.override %{buildroot}%{_datadir}/glib-2.0/schemas/

%postun
if [ $1 -eq 0 ] ; then
    glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :
fi

%posttrans
glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :


%files
%defattr(-,root,root,-)
%config %attr(0644,root,root) /etc/ozon-release
%{_datadir}/glib-2.0/schemas/org.ozonos.gschema.override

%changelog
* Sat Feb 18 2015 Satyajit Sahoo <satya164@fedoraproject.org> - 0.0-1
- Initial package for Fedora

