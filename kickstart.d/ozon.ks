# Kickstart file for Ozon beta
# CAUTION - We need to test the generated .ISO file. Don't "well ... duh" me, it is important

version=Beta
#What the heck these KS files do here, I've no idea
#ks=http://127.0.0.1/ks.cfg
#ks=http://localhost/ks.cfg

# I guess we should replace that with Ozon's .iso link?
url --url http://mirrors.kernel.org/fedora/releases/21/Workstation/x86_64/iso/

#Shitload of services
services --enabled=ksmtuned,lirc,NetworkManager,restorecond,spice-vdagentd --disabled=abrtd,abrt-ccpp,abrt-oops,abrt-vmcore,abrt-xorg,capi,iprdump,iprinit,iprupdate,iscsi,iscsid,isdn,libvirtd,multipathd,netfs,network,nfs,nfslock,pcscd,rpcbind,rpcgssd,rpcidmapd,rpcsvcgssd,sendmail,sm-client,sshd

#Include repos
%include %%KP_KICKSTART_DIR%%/ozon-repos.ks

#Not sure if that means booting from CD room or installing cd room components. If latter it and the #usb option must be without a #
#cdrom
#usb

#Because "u" matters
lang en_GB.UTF-8
#Should change that to grumpy US layout. Sigh.
keyboard gb

#I hope that using just the activate on boot flag will make it aumomagically detect connection type and jada jada
network --onboot yes 

#Figured defaulting to GMT would be the sanest option
timezone --utc Europe/London

# Whatever the hell rootpw is supposed to be
# rootpw  --iscrypted $6$s9i1bQbmW4oSWMJc$0oHfSz0b/d90EvHx7cy70RJGIHrP1awzAgL9A3x2tbkyh72P3kN41vssaI3/SJf4Y4qSo6zxc2gZ3srzc4ACX1

#Some security stuff
selinux --permissive
authconfig --enableshadow --passalgo=sha512 --enablefingerprint
# I take it we don't need firewall, right? 
#firewall --service=ssh

#NOTE - I think this hardcodes installer values about repos and bootloader, so we don't really need them.

# The following is the partition information you requested
# Note that any partitions you deleted are not expressed
# here so unless you clear all partitions first, this is
# not guaranteed to work

#I am deleting the old partitions with this
#clearpart --all --drives=sda

#I am creating partitions here
#I will create the lvm stuff farther down
#part /boot --fstype=ext4 --size=500 --ondisk=sda --asprimary
#part pv.5xwrsR-ldgG-FEmM-2Zu5-Jn3O-sx9T-unQUOe --grow --size=500 --ondisk=sda --asprimary

#Very important to have the two part lines before the lvm stuff
#volgroup VG --pesize=32768 pv.5xwrsR-ldgG-FEmM-2Zu5-Jn3O-sx9T-unQUOe
#logvol / --fstype=ext4 --name=lv_root --vgname=VG --size=40960
#logvol /home --fstype=ext4 --name=lv_home --vgname=VG --size=25600
#logvol swap --fstype swap --name=lv_swap --vgname=VG --size=4096

#bootloader --location=mbr --driveorder=sda --append="rhgb quiet"

%packages
@admin-tools
#Not sure about that standard
@standard
@fonts
@gnome-desktop
@hardware-support
@input-methods
@online-docs
@printing
@base-x
gdm
ozon-repos
ozon-repos-extra
ozon-desktop
#We uninstall gThumb and Steam and install eog for the beta
-gthumb
-steam
eog
#Some driver
b43-firmware
%end

#Shouldn't that kickstart the installation? Pun so not intended. LOL.
install

#During rbeooting ask the use to eject the live DVD if he/she still uses that stuff.
eject
