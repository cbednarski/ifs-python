version = '5.0.0'
version_cmd = 'VBoxManage -v'
depends=['dkms']
download_url = 'http://download.virtualbox.org/virtualbox/5.0.0/virtualbox-5.0_5.0.0-101573~Ubuntu~trusty_amd64.deb'
install_script = """
dpkg -i http://download.virtualbox.org/virtualbox/5.0.0/virtualbox-5.0_5.0.0-101573~Ubuntu~trusty_amd64.deb
apt-get install -fy
"""
