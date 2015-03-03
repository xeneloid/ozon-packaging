Name:		ozon-repos
Version:	21
Release:	4%{?dist}
Summary:	Repositories for Ozon OS.
Group:		System Environment/Base

License:	GPL-3
URL:		http://ozonos.github.io

Requires:       system-release >= %{version}

BuildArch:  noarch

%description
 Default repositories used in Ozon OS.


%install
%{__install} -d -m755 %{buildroot}%{_sysconfdir}/yum.repos.d
cat << EOF >>%{buildroot}%{_sysconfdir}/yum.repos.d/ozonos.repo
[ozonos]
name=Repository for Ozon OS
baseurl=http://goodies.ozon-os.com/repo/\$releasever/
enabled=1
skip_if_unavailable=1
metadata_expire=7d
gpgcheck=1
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-ozonos
EOF

%{__install} -d -m755 %{buildroot}%{_sysconfdir}/pki/rpm-gpg
cat << EOF >>%{buildroot}%{_sysconfdir}/pki/rpm-gpg/RPM-GPG-KEY-ozonos
-----BEGIN PGP PUBLIC KEY BLOCK-----
Version: GnuPG v1

mQENBFT2FUcBCADdGrJ/3KzPOX6jJGHHBfaT23S3UJxBa1wqa7xHDtMQlO8uc+ms
tb9SSdDFaWmxfFWxEQrSZlMxZhlRhv6d5MlLTJPtjIPxri4yEfo0JWsyXHMyHNz9
16k2R9AM7FesPWbC6QGLL3g2CPp/t8zhxor6fLi5yplr5VsyHbpLuOcz0yZCc+D4
n9D1W+BLMjMidzTPfPCoUNBlEtT9//aHvFDhgnB0R59suXNMW7qM74/Cghr//u88
gqxZOBVVchdSVt/aCnP6Hiql6/bq5a6wJn5FVTB5DuWxuD/OZxwbqlyZsnaFnRwE
hTaFdvyN7XVZWojBv23xxkQT2sSNavbFK5FTABEBAAG0PE96b24gT1MgKEdQRyBr
ZXkgZm9yIHRoZSBPem9uIE9TIHByb2plY3QpIDxvem9uQG96b24tb3MuY29tPokB
OAQTAQIAIgUCVPYVRwIbAwYLCQgHAwIGFQgCCQoLBBYCAwECHgECF4AACgkQ3IHn
y7jA/CIjhQf/Riw+OFcPbPbhdB4jRi6u5y3gyzyTNrP8YzYFqNDx7Z6ncR1DClA/
bciOwzq4tBFcAl8xM1B8W0WFe18vXtFdvduKZdKnPBCwthixckItekAeyVm4GrOJ
8K7w5l+hJ1/LCsCC/raLEMYwF0c57mryLFPLzHtsgMD7u2hs9ofgU9/OeA6OnS8y
r8LPfl6iAQo+ybLeu7KRyUnV5ZWfj2m/4ueecKYX3E1ZLYS1mesckyblDAufEvfK
P23NGO+2W1kiQ+JRwn3ka7w7w3jv+mP4h/lpSMbmHgShmNYap8ShHrRt+1AT44/I
Ediq4E2Ls25DuZrb6V5srh5ldUHWiwfZ2LkBDQRU9hVHAQgArmTF0aXBpqjEsFlu
V13gftHJihggnpyzY2FRB6Hocfyv1IE71kCV7OECj0CxT76bYJCjOz0VcZXw5Yap
CMC1Kw1PRA4xx3S/I+kncw1wgjR3x8zY+0xA36lXR1ABlrOxavhcu2ij7ASNSXcm
1DByLIzNG1k9ntfRoQtERfblGt239HsDQeILFPmHXrq0KFRML5IUbOQPMIklUiYN
PeMHlCjg+7BBPhZp5n/zXi4EAs6nfQmttu1bgIu7KYBxXWzKq0RQosm6luTBNj7P
gYtHP6z42RFII/6BCfhrVncaScTr9+MITwJABxIqu775nUTiJDPKoVlgaBKTIfd1
w9MIJQARAQABiQEfBBgBAgAJBQJU9hVHAhsMAAoJENyB58u4wPwiz48IAKDcXvKz
PqHu2igInWzdWURz0vK4l/L2RBK/pbGNykzNOQFhe4q+vCJfIF8klwpH4q1t9qwu
Anq9giGKPNFoXEq5D+0ZziPHr7UHIXAFK0fOW5RRFNpRwEOFhiy/s0nBRQAttAAs
MNyTDXswqyEGYBRrJPRv7q68pTMHixBaegX4vKpyOZy2jhrMgejG8ezpOi6M1Pxv
3sRXnm5HWHuDTOVa9T52s+c5TvhG06FGf3N/VQLh8x5C8XTX+PtbdsG0DO2iEsDG
EOcUmktDZpnuhnhhpekca5tcPKpz/kTLm536aCizpAoZz9amdwJ17cfCeRq5QOrQ
YLiQNLaewOiNy84=
=r6Mg
-----END PGP PUBLIC KEY BLOCK-----
EOF


%files
%defattr(-,root,root)
%config(noreplace) %{_sysconfdir}/yum.repos.d/ozonos.repo
%{_sysconfdir}/pki/rpm-gpg/RPM-GPG-KEY-ozonos

%changelog
* Tue Feb 17 2015 Satyajit Sahoo <satya164@fedoraproject.org> - 0.0-1
- Initial package for Fedora

