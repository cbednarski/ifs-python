version=''
version_cmd=''
depends=['build-essential']
download_url=''
install_script="""
echo "This installer is broken :("
echo "Please help fix it: https://github.com/cbednarski/ifs/issues/9"
# apt-get install -y libpcre3-dev zlib1g-dev libssl-dev
# cd /tmp
# wget -q http://www.haproxy.org/download/1.5/src/haproxy-1.5.3.tar.gz
# tar -xzf haproxy-1.5.3.tar.gz
# cd /tmp/haproxy-1.5.3
# make TARGET=generic USE_TFO=1 USE_PCRE=1 USE_STATIC_PCRE=1 USE_PCRE_JIT=1 USE_OPENSSL=1
# make install
# haproxy -v
exit 1
"""