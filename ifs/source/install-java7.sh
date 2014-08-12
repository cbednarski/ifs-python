if ! java -version ; then
  JAVA_FILE=jdk-7u67-linux-x64.tar.gz
  cd /tmp
  # -s/--silent -L/--location -b/--cookie
  curl -s -L -b 'oraclelicense=accept-securebackup-cookie' http://download.oracle.com/otn-pub/java/jdk/7u67-b01/$JAVA_FILE -o $JAVA_FILE
  tar -xzf $JAVA_FILE
  cd /tmp/jdk1.7.0_67
fi