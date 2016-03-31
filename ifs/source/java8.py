version = '1.8.0_77'
version_cmd = 'java -version'
version_re = 'java version "(\d+\.\d+\.\d+_\d+)"'
description = "Oracle Java 8"
install_script = """
wget -nv --header "Cookie: oraclelicense=accept-securebackup-cookie" -O jdk-8u77-linux-x64.tar.gz http://download.oracle.com/otn-pub/java/jdk/8u77-b03/jdk-8u77-linux-x64.tar.gz
rm -rf jdk1.8.0_77/
tar -xzf jdk-8u77-linux-x64.tar.gz
rm -rf /opt/jdk1.8.0_77
mv jdk1.8.0_77/ /opt
echo "export JAVA_HOME=/opt/jdk1.8.0_77\nexport PATH=\$PATH:\$JAVA_HOME/bin" > /etc/profile.d/oracle-java8.sh
grep "/opt/jdk1.8.0_77" /etc/bash.bashrc >/dev/null || echo "export JAVA_HOME=/opt/jdk1.8.0_77\nexport PATH=\$PATH:\$JAVA_HOME/bin" >> /etc/bash.bashrc
"""
