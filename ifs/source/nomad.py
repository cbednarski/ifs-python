version = '0.3.2'
version_cmd = 'nomad -v'
depends = ['unzip']
download_url = 'https://releases.hashicorp.com/nomad/VERSION/nomad_VERSION_linux_amd64.zip'
install_script = """
unzip -o nomad_VERSION_linux_amd64.zip
mv -f nomad /usr/local/bin/nomad
"""
