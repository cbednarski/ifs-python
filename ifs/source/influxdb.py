version_cmd = 'influxdb -v'
download_url = 'http://s3.amazonaws.com/influxdb/influxdb_latest_amd64.deb'
install_script = """
dpkg -i influxdb_latest_amd64.deb
service influxdb start
"""
