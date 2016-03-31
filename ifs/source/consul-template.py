version = '0.14.0'
version_cmd = 'consul-template -v'
depends = ['unzip']
download_url = 'https://releases.hashicorp.com/consul-template/VERSION/consul-template_VERSION_linux_amd64.zip'
install_script = """
unzip -o consul-template_VERSION_linux_amd64.zip
mv -f consul-template /usr/local/bin/consul-template
"""
