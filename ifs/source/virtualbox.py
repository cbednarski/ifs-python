version = '5.1.8'
version_cmd = 'VBoxManage -v'
depends=['dkms', 'libgl1-mesa-glx', 'libqt4-network', 'libqt4-opengl', 'libqtcore4', 'libqtgui4', 'libsdl1.2debian', 'libvpx1', 'libxcursor1', 'libxinerama1']
download_url = 'http://download.virtualbox.org/virtualbox/5.1.8/virtualbox-5.1_5.1.8-111374~Ubuntu~xenial_amd64.deb'
install_script = """
# Installation may fail because of missing dependencies, but we can resolve this afterward.
dpkg -i virtualbox-5.1_5.1.8-111374~Ubuntu~xenial_amd64.deb || true
apt-get install -fy
"""
