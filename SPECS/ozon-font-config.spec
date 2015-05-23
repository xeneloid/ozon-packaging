Summary:	Ozon font configuration
Name:		ozon-font-config
Version:	%{fedora}
Release:	1%{?dist}

License:	GPL-3
Group:		System Environment/Base

URL:		http://ozonos.github.io

Requires:	freetype-freeworld
Requires:	google-noto-sans-fonts

BuildArch:	noarch

%description
Font configuration for Ozon desktop.


%install
%{__install} -d -m755 %{buildroot}/etc/fonts/
cat << EOF >>%{buildroot}/etc/fonts/local.conf
<?xml version="1.0"?>
<!DOCTYPE fontconfig SYSTEM "fonts.dtd">
<fontconfig>
 <match target="pattern">
  <edit name="dpi" mode="assign">96</edit>
 </match>
 <match target="font">
  <edit mode="assign" name="antialias" >
  <bool>true</bool>
  </edit>
 </match>
 <match target="font">
  <edit mode="assign" name="hinting" >
  <bool>true</bool>
  </edit>
 </match>
 <match target="font">
  <edit mode="assign" name="hintstyle" >
  <const>hintslight</const>
  </edit>
 </match>
 <match target="font">
  <edit mode="assign" name="rgba" >
  <const>rgb</const>
  </edit>
 </match>
 <match target="font">
  <edit mode="assign" name="lcdfilter">
  <const>lcddefault</const>
  </edit>
 </match>
 </fontconfig>
EOF


%files
%defattr(-,root,root,-)
%config %attr(0644,root,root) /etc/fonts/local.conf


%changelog
* Tue Feb 17 2015 Satyajit Sahoo <satya164@fedoraproject.org> - 0.0-1
- Initial package for Fedora

