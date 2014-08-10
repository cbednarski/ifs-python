if ! java -version ; then
  cd /tmp
  curl -q -L --cookie 'oraclelicense=accept-securebackup-cookie' http://download.oracle.com/otn-pub/java/jdk/7u67-b01/jdk-7u67-linux-x64.tar.gz -o jdk-7u67-linux-x64.tar.gz
  tar -xzf jdk-7u67-linux-x64.tar.gz
  cd /tmp/jdk1.7.0_67
fi