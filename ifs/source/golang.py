version = '1.5.1'
version_cmd = 'go version'
download_url = 'https://storage.googleapis.com/golang/goVERSION.linux-amd64.tar.gz'
install_script = """
tar -C /usr/local -xzf goVERSION.linux-amd64.tar.gz
echo "export PATH=\$PATH:/usr/local/go/bin" > /etc/profile.d/golang.sh
grep "/usr/local/go/bin" /etc/bash.bashrc >/dev/null || echo "export PATH=\$PATH:/usr/local/go/bin" >> /etc/bash.bashrc
"""
