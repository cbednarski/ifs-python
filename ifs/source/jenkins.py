version_cmd = 'java -jar /usr/share/jenkins/jenkins.war --version'
version_re = '(\d\.\d{3})'
depends = ['wget']
install_script = """
wget -q -O - http://pkg.jenkins-ci.org/debian/jenkins-ci.org.key | apt-key add -
echo "deb http://pkg.jenkins-ci.org/debian binary/" > /etc/apt/sources.list.d/jenkins.list
apt-get update
apt-get install -y jenkins
"""
