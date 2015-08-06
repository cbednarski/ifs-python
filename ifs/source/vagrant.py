version = '1.7.4'
version_cmd = 'vagrant -v'
download_url = 'https://dl.bintray.com/mitchellh/vagrant/vagrant_VERSION_x86_64.deb'
install_script = """
dpkg -i vagrant_VERSION_x86_64.deb
"""
