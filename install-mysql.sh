if ! mysqld --version ; then
  cd /tmp
  wget -q wget http://dev.mysql.com/get/Downloads/MySQL-5.6/mysql-5.6.19-debian6.0-x86_64.deb
  dpkg -i mysql-5.6.19-debian6.0-x86_64.deb
fi