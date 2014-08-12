version='1.6.1'
version_cmd='nginx -v'
depends=['build-essentials', 'libpcre3-dev', 'zlib1g-dev', 'libssl-dev']
download_url='http://nginx.org/download/nginx-VERSION.tar.gz'
install_script="""
tar -xzf nginx-1.6.0.tar.gz
cd nginx-1.6.0/
./configure \
    --with-http_ssl_module \
    --with-http_auth_request_module \
    --prefix=/etc/nginx \
    --conf-path=/etc/nginx/nginx.conf \
    --sbin-path=/usr/sbin/nginx \
    --pid-path=/var/run/nginx.pid \
    --error-log-path=/var/log/nginx/error.log \
    --http-log-path=/var/log/nginx/access.log
make
make install

mkdir -p /etc/nginx/sites-enabled
chmod -R 0755 /etc/nginx
"""