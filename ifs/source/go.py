version = '1.6.2'
version_cmd = 'go version'
version_re = 'go version go([\d\.]+)'
download_url = 'https://storage.googleapis.com/golang/goVERSION.linux-amd64.tar.gz'
install_script = """
rm -rf /usr/local/go
tar -C /usr/local -xzf goVERSION.linux-amd64.tar.gz
echo "export PATH=\$PATH:/usr/local/go/bin" > /etc/profile.d/golang.sh
grep "/usr/local/go/bin" /etc/bash.bashrc >/dev/null || echo "export PATH=\$PATH:/usr/local/go/bin" >> /etc/bash.bashrc
"""
