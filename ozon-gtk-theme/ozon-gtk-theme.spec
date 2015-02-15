%global theme	Ozon

Name:		ozon-gtk-theme
Version:	0.1
Release:	alpha1%{?dist}
Summary:	%{theme} GTK theme for Gnome
Group:		User Interface/Desktops

License:	GPL-3
URL:		http://fav.me/d5ygul6
Source0:	ozon-gtk-theme.tar.gz

BuildRequires:	rubygem-sass >= 3.4.0

Requires:	gtk-murrine-engine >= 0.98.1.1
Requires:	gtk3 >= 3.14.0

BuildArch:	noarch

%description
%{theme} is the official GTK theme for Ozon OS.


%prep
%setup -q -n %{name}-master

%build
make %{?_smp_mflags}

%install
%make_install


%files
%defattr(-,root,root)
%doc CREDITS LICENSE README.md
%{_datadir}/themes/%{theme}


%changelog
* Sat Feb 16 2015 Satyajit Sahoo <satya164@fedoraproject.org> - 0.0-1
- Initial package for Fedora

