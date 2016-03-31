version = '3.0.7'
version_cmd = 'redis-server -v'
depends = ['build-essential']
download_url = 'http://download.redis.io/releases/redis-VERSION.tar.gz'
install_script = """
tar -xzf redis-VERSION.tar.gz
cd redis-VERSION/
make
make install
"""
