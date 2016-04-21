version = '0.11.0'
version_cmd = 'confd -version'
download_url = 'https://github.com/kelseyhightower/confd/releases/download/vVERSION/confd-VERSION-linux-amd64'
install_script = """
chmod +x confd-VERSION-linux-amd64
mv -f confd-VERSION-linux-amd64 /usr/local/bin/confd
"""
