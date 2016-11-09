version = '1.8.7'
version_cmd = 'vagrant -v'
download_url = 'https://dl.bintray.com/mitchellh/vagrant/vagrant_VERSION_x86_64.deb'
install_script = """
dpkg -i vagrant_VERSION_x86_64.deb
"""
