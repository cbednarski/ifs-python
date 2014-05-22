# Mongodb
if brew -v && ! mongo --version ; then
  brew install mongodb
  exit
fi

if ! mongo --version ; then
  apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 7F0CEB10
  echo 'deb http://downloads-distro.mongodb.org/repo/ubuntu-upstart dist 10gen' >> /etc/apt/sources.list.d/mongodb.list
  apt-get update
  apt-get install -y mongodb-org
fi