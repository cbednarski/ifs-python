version = '1.11.0'
version_cmd = 'docker -v'
depends = ['apt-transport-https']
install_script = """
echo deb https://apt.dockerproject.org/repo ubuntu-`lsb_release -c | awk '{print $2}'` main > /etc/apt/sources.list.d/docker.list
apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys 58118E89F3A912897C070ADBF76221572C52609D
apt-get update -o Dir::Etc::sourcelist="sources.list.d/docker.list" -o Dir::Etc::sourceparts="-" -o APT::Get::List-Cleanup="0"
apt-get install -y docker-engine
"""
