version_cmd = 'mysqld --version'
version_re = '(\d+\.\d+\.\S+).+Percona Server'
install_script = """
apt-key adv --keyserver keys.gnupg.net --recv-keys 1C4CBDCDCD2EFD2A
echo "deb http://repo.percona.com/apt trusty main
deb-src http://repo.percona.com/apt trusty main" > /etc/apt/sources.list.d/percona.list
apt-get update -qq
DEBIAN_FRONTEND=noninteractive apt-get install -y percona-server-server percona-server-client

mysql -e "CREATE FUNCTION fnv1a_64 RETURNS INTEGER SONAME 'libfnv1a_udf.so'" || true
mysql -e "CREATE FUNCTION fnv_64 RETURNS INTEGER SONAME 'libfnv_udf.so'" || true
mysql -e "CREATE FUNCTION murmur_hash RETURNS INTEGER SONAME 'libmurmur_udf.so'" || true
"""
