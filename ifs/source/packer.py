version = '0.10.0'
version_cmd = 'packer version'
version_re = 'Packer v(\d+\.\d+\.\d+).*'
depends = ['unzip']
download_url = 'https://releases.hashicorp.com/packer/VERSION/packer_VERSION_linux_amd64.zip'
install_script = """
  unzip -o packer_VERSION_linux_amd64.zip
  chmod +x packer
  mv packer /usr/local/bin/packer
"""
