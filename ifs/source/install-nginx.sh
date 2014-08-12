if ! nginx -v ; then
  apt-get install -y build-essentials libpcre3-dev zlib1g-dev libssl-dev
  cd /tmp
  wget -q http://nginx.org/download/nginx-1.6.0.tar.gz
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
fi