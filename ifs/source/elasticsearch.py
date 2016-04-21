version = '2.3.1'
version_cmd = 'elasticsearch -version'
download_url = 'http://packages.elasticsearch.org/GPG-KEY-elasticsearch'
install_script = """
apt-key add GPG-KEY-elasticsearch
echo "deb http://packages.elasticsearch.org/elasticsearch/VERSION/debian stable main" > /etc/apt/sources.list.d/elasticsearch.list
apt-get update -qq
apt-get install -y elasticsearch
service elasticsearch start
"""
