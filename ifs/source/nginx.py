version='1.6.2'
version_cmd='nginx -v'
depends=['build-essential', 'libpcre3-dev', 'zlib1g-dev', 'libssl-dev']
download_url='http://nginx.org/download/nginx-VERSION.tar.gz'

upstart="""
# Based on http://upstart.ubuntu.com/cookbook/
# and http://nginx.org/en/docs/control.html
start on runlevel [2345]
stop on runlevel [016]

expect fork

pre-start exec nginx -t
pre-stop exec nginx -s quit

reload signal SIGHUP

exec nginx
"""

install_script="""
tar -xzf nginx-VERSION.tar.gz
cd nginx-VERSION/
# See http://wiki.nginx.org/Modules for more
./configure \
    --with-http_ssl_module \
    --prefix=/etc/nginx \
    --conf-path=/etc/nginx/nginx.conf \
    --sbin-path=/usr/sbin/nginx \
    --pid-path=/var/run/nginx.pid \
    --error-log-path=/var/log/nginx/error.log \
    --http-log-path=/var/log/nginx/access.log
make
make install

mkdir -p /etc/nginx/sites-enabled
chmod -R 0700 /etc/nginx
"""

# def install(c):
#     # c.call
#     pass

