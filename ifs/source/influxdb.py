version='0.8.1'
version_cmd='influxdb -v'
download_url='http://s3.amazonaws.com/influxdb/influxdb_latest_amd64.deb'
install_script="""
sudo dpkg -i influxdb_latest_amd64.deb
"""