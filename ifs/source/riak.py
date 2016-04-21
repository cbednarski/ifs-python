version = '2.1.4'
version_cmd = 'riak version'
download_url = 'http://s3.amazonaws.com/downloads.basho.com/riak/2.1/2.1.1/ubuntu/trusty/riak_2.1.1-1_amd64.deb'
install_script = """
dpkg -i riak_2.1.1-1_amd64.deb
"""
