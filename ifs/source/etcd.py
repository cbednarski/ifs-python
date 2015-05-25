version = '0.4.6'
version_cmd = 'etcd -version'
download_url = 'https://github.com/coreos/etcd/releases/download/vVERSION/etcd-vVERSION-linux-amd64.tar.gz'
install_script = """
tar -xzf etcd-vVERSION-linux-amd64.tar.gz
mv -f ./etcd-v0.4.6-linux-amd64/etcd /usr/local/bin/etcd
mv -f ./etcd-v0.4.6-linux-amd64/etcdctl /usr/local/bin/etcdctl
"""
