version = '1.6.4'
version_cmd = 'haproxy -v'
depends = ['build-essential', 'libpcre3-dev', 'zlib1g-dev', 'libssl-dev']
download_url = 'http://www.haproxy.org/download/1.6/src/haproxy-VERSION.tar.gz'

upstart = """
start on runlevel [2345]
stop on runlevel [016]

expect fork

pre-start exec haproxy -t
pre-stop exec haproxy -s quit

reload signal SIGHUP

exec haproxy
"""

install_script = """
echo "This installer is broken :("
echo "Please help fix it: https://github.com/cbednarski/ifs/issues/9"
# tar -xzf haproxy-VERSION.tar.gz
# cd haproxy-VERSION
# make TARGET=generic USE_TFO=1 USE_PCRE=1 USE_STATIC_PCRE=1 USE_PCRE_JIT=1 USE_OPENSSL=1
# make install
# if [ ! -d /etc/haproxy ] ; then mkdir -p /etc/haproxy ; fi
# cp examples/haproxy.cfg /etc/haproxy/haproxy.cfg
# haproxy -v
exit 1
"""
