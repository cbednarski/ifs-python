version = '0.5.2'
version_cmd = 'consul -v'
depends = ['unzip']
download_url = 'https://dl.bintray.com/mitchellh/consul/VERSION_linux_amd64.zip'
install_script = """
unzip -o VERSION_linux_amd64.zip
mv -f consul /usr/local/bin/consul
"""
