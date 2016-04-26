version = '2.3.1'
version_cmd = 'rethinkdb -v'
depends = ['apt-transport-https']
install_script = """
echo deb https://download.rethinkdb.com/apt `lsb_release -c | awk '{print $2}'` main > /etc/apt/sources.list.d/rethinkdb.list
wget -qO- https://download.rethinkdb.com/apt/pubkey.gpg | apt-key add -
apt-get update -o Dir::Etc::sourcelist="sources.list.d/rethinkdb.list" -o Dir::Etc::sourceparts="-" -o APT::Get::List-Cleanup="0"
apt-get install -y rethinkdb
"""
