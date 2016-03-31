version = '0.5.2'
version_cmd = 'vault -v'
depends = ['unzip']
download_url = 'https://releases.hashicorp.com/vault/VERSION/vault_VERSION_linux_amd64.zip'
install_script = """
unzip -o vault_VERSION_linux_amd64.zip
mv -f vault /usr/local/bin/vault
"""
