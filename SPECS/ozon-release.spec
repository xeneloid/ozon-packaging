%define codename Hydrogen

Summary:	Ozon release files
Name:		ozon-release
Version:	%{fedora}
Release:	3%{?dist}
License:	MIT
Group:		System Environment/Base

URL:		http://ozonos.github.io
Requires:	fedora-release = %{version}

BuildArch:	noarch

%description
Ozon release files and default settings.


%install
%{__install} -d -m755 %{buildroot}/etc
echo "Ozon release %{version} (%{codename})" > %{buildroot}/etc/ozon-release
%{__install} -d -m755 %{buildroot}%{_datadir}/glib-2.0/schemas/
cat << EOF >>%{buildroot}%{_datadir}/glib-2.0/schemas/org.ozonos.gschema.override
[org.gnome.desktop.interface]
font-name='Noto Sans 10'
gtk-theme='Ozon'
icon-theme='Ozon'

[org.gnome.desktop.wm.preferences]
theme='Ozon'
titlebar-font='Noto Sans Bold 10'

[org.gnome.shell]
enabled-extensions=['user-theme@gnome-shell-extensions.gcampax.github.com', 'atom-dock@ozonos.org', 'atom-launcher@ozonos.org', 'atom-panel@ozonos.org']
favorite-apps=['org.gnome.Nautilus.desktop', 'chromium-browser.desktop', 'rhythmbox.desktop', 'org.gnome.Software.desktop']

[org.gnome.shell.extensions.user-theme]
name='Ozon'

[org.gnome.settings-daemon.plugins.xsettings]
hinting='slight'
antialiasing='rgba'

[org.gnome.nautilus.icon-view]
default-zoom-level='small'
captions=['size', 'type', 'date_modified']

[org.gnome.nautilus.preferences]
click-policy='single'
EOF

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
* Wed Feb 18 2015 Satyajit Sahoo <satya164@fedoraproject.org> - 0.0-1
- Initial package for Fedora

