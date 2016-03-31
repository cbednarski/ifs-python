version = '0.6.1'
version_cmd = 'envconsul -v'
depends = ['unzip']
download_url = 'https://releases.hashicorp.com/envconsul/VERSION/envconsul_VERSION_linux_amd64.zip'
install_script = """
unzip -o envconsul_VERSION_linux_amd64.zip
mv -f envconsul /usr/local/bin/envconsul
"""
