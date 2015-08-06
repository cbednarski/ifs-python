version = '1.8.0_51'
version_cmd = 'java -version'
description = "Oracle Java 8"
install_script = """
wget --header "Cookie: oraclelicense=accept-securebackup-cookie" http://download.oracle.com/otn-pub/java/jdk/8u51-b16/jdk-8u51-linux-x64.tar.gz
tar -xzf jdk-8u51-linux-x64.tar.gz
mv jdk1.8.0_51/ /opt
echo "export JAVA_HOME=/opt/jdk1.8.0_51\nexport PATH=\$PATH:\$JAVA_HOME/bin" > /etc/profile.d/oracle-java8.sh
grep "/opt/jdk1.8.0_51" /etc/bash.bashrc >/dev/null || echo "export JAVA_HOME=/opt/jdk1.8.0_51\nexport PATH=\$PATH:\$JAVA_HOME/bin" >> /etc/bash.bashrc
"""
