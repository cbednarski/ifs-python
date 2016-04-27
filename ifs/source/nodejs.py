version = '6.0.0'
version_cmd = 'node -v'
download_url = 'http://nodejs.org/dist/vVERSION/node-vVERSION-linux-x64.tar.gz'
install_script = """
  tar --strip-components 1 -C /usr/local -xzf node-vVERSION-linux-x64.tar.gz
"""
