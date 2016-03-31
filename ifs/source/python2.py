version = '2.7.11'
version_cmd = 'python -v'
# depends=['build-essential', 'libpcre3-dev', 'zlib1g-dev', 'libssl-dev']
download_url = 'https://www.python.org/ftp/python/VERSION/Python-VERSION.tgz'
install_script = """
tar -xzf Python-VERSION.tgz
cd Python-VERSION/
./configure
make
make altinstall
"""
