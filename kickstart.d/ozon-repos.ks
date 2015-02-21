# REPOS

#Stolen from Korora, may need fixing

# Base ozon repo
repo --name="Repository for Ozon OS" --baseurl=http://goodies.ozon-os.com/repo/$releasever/ --cost=1000

# Chormium repo
#repo --name="Copr repo for chromium owned by spot" --baseurl=https://copr-be.cloud.fedoraproject.org/results/spot/chromium/fedora-$releasever-$basearch/ --cost=1000

#Basic Fedora repos
repo --name="Fedora %%KP_VERSION%% - %%KP_BASEARCH%%" --baseurl=http://dl.fedoraproject.org/pub/fedora/linux/releases/%%KP_VERSION%%/Everything/%%KP_BASEARCH%%/os/ --cost=1000
repo --name="Fedora %%KP_VERSION%% - %%KP_BASEARCH%% - Updates" --baseurl=http://dl.fedoraproject.org/pub/fedora/linux/updates/%%KP_VERSION%%/%%KP_BASEARCH%%/ --cost=1000
#repo --name="Fedora %%KP_VERSION%% - %%KP_BASEARCH%% - Updates Testing" --baseurl=http://download.fedoraproject.org/pub/fedora/linux/updates/testing/%%KP_VERSION%%/%%KP_BASEARCH%%/ --cost=1000

#RPM Fusion stuff
repo --name="RPMFusion Free" --baseurl=http://download1.rpmfusion.org/free/fedora/releases/%%KP_VERSION%%/Everything/%%KP_BASEARCH%%/os/ --cost=1000
repo --name="RPMFusion Free - Updates" --baseurl=http://download1.rpmfusion.org/free/fedora/updates/%%KP_VERSION%%/%%KP_BASEARCH%%/ --cost=1000

repo --name="RPMFusion Non-Free" --baseurl=http://download1.rpmfusion.org/nonfree/fedora/releases/%%KP_VERSION%%/Everything/%%KP_BASEARCH%%/os/ --cost=1000
repo --name="RPMFusion Non-Free - Updates" --baseurl=http://download1.rpmfusion.org/nonfree/fedora/updates/%%KP_VERSION%%/%%KP_BASEARCH%%/ --cost=1000
#repo --name="VirtualBox" --baseurl=http://download.virtualbox.org/virtualbox/rpm/fedora/%%KP_VERSION%%/%%KP_BASEARCH%%/ --cost=1000

#repo --name="RPMFusion Free - Development" --baseurl=http://download1.rpmfusion.org/free/fedora/development/%%KP_VERSION%%/%%KP_BASEARCH%%/os/ --cost=1000
#repo --name="RPMFusion Non-Free - Development" --baseurl=http://download1.rpmfusion.org/nonfree/fedora/development/%%KP_VERSION%%/%%KP_BASEARCH%%/os/ --cost=1000
# RAWHIDE - use when RPM Fusion has not yet branched (usually because fedora is still pre-beta)
#repo --name="RPMFusion Free - Development" --baseurl=http://download1.rpmfusion.org/free/fedora/development/rawhide/%%KP_BASEARCH%%/os/ --cost=1000
#repo --name="RPMFusion Non-Free - Development" --baseurl=http://download1.rpmfusion.org/nonfree/fedora/development/rawhide/%%KP_BASEARCH%%/os/ --cost=1000

