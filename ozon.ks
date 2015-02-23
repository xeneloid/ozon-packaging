%include /usr/share/spin-kickstarts/fedora-live-base.ks

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
-@dial-up
-@input-methods
-@standard

@base-x
@core
@fonts
@guest-desktop-agents
@hardware-support
@multimedia
@networkmanager-submodules
@printing

# Exclude unwanted packages from @anaconda-tools group
-gfs2-utils
-reiserfs-utils

# Install Ozon desktop
ozon-repos
ozon-repos-extra
ozon-desktop

gcc
gcc-c++
akmod-wl
isight-firmware-tools
eog
gnome-screenshot

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

%post

# This is a huge file and things work ok without it
rm -f /usr/share/icons/HighContrast/icon-theme.cache

cat >> /etc/rc.d/init.d/livesys << EOF


# disable updates plugin
cat >> /usr/share/glib-2.0/schemas/org.gnome.software.gschema.override << FOE
[org.gnome.software]
download-updates=false
FOE

# don't run gnome-initial-setup
mkdir ~liveuser/.config
touch ~liveuser/.config/gnome-initial-setup-done

# make the installer show up
if [ -f /usr/share/applications/liveinst.desktop ]; then
  # Show harddisk install in shell dash
  sed -i -e 's/NoDisplay=true/NoDisplay=false/' /usr/share/applications/liveinst.desktop ""
  # need to move it to anaconda.desktop to make shell happy
  mv /usr/share/applications/liveinst.desktop /usr/share/applications/anaconda.desktop

  cat >> /usr/share/glib-2.0/schemas/org.gnome.shell.gschema.override << FOE
[org.gnome.shell]
favorite-apps=['org.gnome.Nautilus.desktop', 'chromium.desktop', 'tomahawk.desktop', 'gedit.desktop', 'anaconda.desktop']
FOE

  # Make the welcome screen show up
  if [ -f /usr/share/anaconda/gnome/fedora-welcome.desktop ]; then
    mkdir -p ~liveuser/.config/autostart
    cp /usr/share/anaconda/gnome/fedora-welcome.desktop /usr/share/applications/
    cp /usr/share/anaconda/gnome/fedora-welcome.desktop ~liveuser/.config/autostart/
  fi

  # Copy Anaconda branding in place
  if [ -d /usr/share/lorax/product/usr/share/anaconda ]; then
    cp -a /usr/share/lorax/product/* /
  fi
fi

# rebuild schema cache with any overrides we installed
glib-compile-schemas /usr/share/glib-2.0/schemas

# set up auto-login
cat > /etc/gdm/custom.conf << FOE
[daemon]
AutomaticLoginEnable=True
AutomaticLogin=liveuser
FOE

# Turn off PackageKit-command-not-found while uninstalled
if [ -f /etc/PackageKit/CommandNotFound.conf ]; then
  sed -i -e 's/^SoftwareSourceSearch=true/SoftwareSourceSearch=false/' /etc/PackageKit/CommandNotFound.conf
fi

# make sure to set the right permissions and selinux contexts
chown -R liveuser:liveuser /home/liveuser/
restorecon -R /home/liveuser/

EOF

%end

