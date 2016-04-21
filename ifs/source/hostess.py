version = '0.1.0'
version_cmd = 'hostess -v'
version_re = 'hostess version (\d+\.\d+\.\d+)'
download_url = 'https://github.com/cbednarski/hostess/releases/download/vVERSION/hostess_linux_amd64'
install_script = """
  chmod +x hostess
  mv hostess /usr/local/bin/hostess
"""
