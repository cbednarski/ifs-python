version = '2.0.0'
version_cmd = 'riak version'
download_url = 'http://s3.amazonaws.com/downloads.basho.com/riak/2.0/2.0.0/ubuntu/trusty/riak_2.0.0-1_amd64.deb'
install_script = """
dpkg -i riak_2.0.0-1_amd64.deb
"""
