if ! java -version ; then
  cd /tmp
  curl -q -L --cookie 'oraclelicense=accept-securebackup-cookie' http://download.oracle.com/otn-pub/java/jdk/8u11-b12/jdk-8u11-linux-x64.tar.gz -o jdk-8u11-linux-x64.tar.gz
  tar -xzf jdk-8u11-linux-x64.tar.gz
  cd /tmp/jdk1.8.0_11
fi
