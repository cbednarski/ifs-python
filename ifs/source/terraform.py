version = '0.6.15'
version_cmd = 'terraform version'
version_re = 'Terraform v(\d+\.\d+\.\d+).*'
depends = ['unzip']
download_url = 'https://releases.hashicorp.com/terraform/VERSION/terraform_VERSION_linux_amd64.zip'
install_script = """
  unzip -o terraform_VERSION_linux_amd64.zip
  chmod +x terraform*
  mv terraform* /usr/local/bin/
"""
