%include /usr/share/spin-kickstarts/fedora-live-desktop.ks
selinux --disabled

part / --size 4400

repo --name=rpmfusion-free --baseurl=http://download1.rpmfusion.org/free/fedora/releases/$releasever/Everything/$basearch/os
repo --name=rpmfusion-free-updates --baseurl=http://download1.rpmfusion.org/free/fedora/updates/$releasever/$basearch
repo --name=rpmfusion-non-free  --baseurl=http://download1.rpmfusion.org/nonfree/fedora/releases/$releasever/Everything/$basearch/os
repo --name=rpmfusion-non-free-updates --baseurl=http://download1.rpmfusion.org/nonfree/fedora/updates/$releasever/$basearch

# Base ozon repo
repo --name="Repository for Ozon OS" --baseurl=http://goodies.ozon-os.com/repo/$releasever/ --cost=1000

# Chormium repo
repo --name="Copr repo for chromium owned by spot" --baseurl=https://copr-be.cloud.fedoraproject.org/results/spot/chromium/fedora-$releasever-$basearch/ --cost=1000

%packages
gcc
gcc-c++
kmod-wl
isight-firmware-tools
ozon-repos
ozon-repos-extra
ozon-desktop
eog
-gthumb
-bijiben
-gnome-documents
-gnome-boxes
-gcolor2
-seahorse
-gnome-abrt
-setroubleshoot
-gnome-logs
-vinagre
-ibus
%end

