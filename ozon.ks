%include /usr/share/spin-kickstarts/fedora-live-workstation.ks

selinux --permissive

part / --size 4400

# Base ozon repo
repo --name="Repository for Ozon OS" --baseurl=http://goodies.ozon-os.com/repo/$releasever/ --cost=1000

# RPMFusion repos
repo --name=rpmfusion-free --baseurl=http://download1.rpmfusion.org/free/fedora/releases/$releasever/Everything/$basearch/os
repo --name=rpmfusion-free-updates --baseurl=http://download1.rpmfusion.org/free/fedora/updates/$releasever/$basearch
repo --name=rpmfusion-non-free  --baseurl=http://download1.rpmfusion.org/nonfree/fedora/releases/$releasever/Everything/$basearch/os
repo --name=rpmfusion-non-free-updates --baseurl=http://download1.rpmfusion.org/nonfree/fedora/updates/$releasever/$basearch

# Chormium repo
repo --name="Copr repo for chromium owned by spot" --baseurl=https://copr-be.cloud.fedoraproject.org/results/spot/chromium/fedora-$releasever-$basearch/ --cost=1000

%packages
# Exclude unwanted groups that fedora-live-base.ks pulls in
-@libreoffice

# Install Ozon desktop
ozon-repos
ozon-repos-extra
ozon-desktop

gcc
gcc-c++
akmod-wl
isight-firmware-tools
eog

# Remove unwanted packages
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

