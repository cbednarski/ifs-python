version='4.3.20'
version_cmd='VBoxManage -v'
download_url='http://download.virtualbox.org/virtualbox/4.3.20/virtualbox-4.3_4.3.20-96996~Ubuntu~raring_amd64.deb'
install_script="""
dpkg -i virtualbox-4.3_4.3.20-96996~Ubuntu~raring_amd64.deb || true
apt-get install -fy
"""