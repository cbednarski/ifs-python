version = '0.6.4'
version_cmd = 'consul -v'
depends = ['unzip']
download_url = 'https://releases.hashicorp.com/consul/VERSION/consul_VERSION_linux_amd64.zip'
install_script = """
unzip -o consul_VERSION_linux_amd64.zip
mv -f consul /usr/local/bin/consul
"""
