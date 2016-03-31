version = '3.5.1'
version_cmd = 'python -v'
depends = ['build-essential']
download_url = 'https://www.python.org/ftp/python/VERSION/Python-VERSION.tgz'
install_script = """
tar -xzf Python-VERSION.tgz
cd Python-VERSION/
./configure
make
make altinstall
"""
