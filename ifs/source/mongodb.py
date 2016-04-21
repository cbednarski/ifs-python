name = 'mongodb'
version = '3.2.5'
version_cmd = 'mongod --version'
install_script = '''
apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 7F0CEB10
echo 'deb http://downloads-distro.mongodb.org/repo/ubuntu-upstart dist 10gen' > /etc/apt/sources.list.d/mongodb.list
apt-get update -qq
apt-get install -qy mongodb-org
'''
