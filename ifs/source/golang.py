version = '1.4.2'
version_cmd = 'go version'
download_url = 'https://storage.googleapis.com/golang/goVERSION.linux-amd64.tar.gz'
install_script = """
tar -c /usr/local -xzf goVERSION.linux-amd64.tar.gz
cat "export PATH=$PATH:/usr/local/go/bin" > /etc/profile.d/golang
"""
