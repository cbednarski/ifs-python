version='2.8.17'
version_cmd='redis-server -v'
depends=['build-essential']
download_url='http://download.redis.io/releases/redis-VERSION.tar.gz'
def installer():
    shell('tar -xzf redis-VERSION.tar.gz')
    cd('redis-VERSION/')
    shell('make')
    shell('make install')
    mkdir('/etc/redis')
    mkdir('/var/redis')
    cp('utils/redis_init_script', '/etc/init.d/redis_6379', replace=False)
    cp('redis.conf', '/etc/redis/6379.conf', replace=False)
    shell('update-rc.d redis_6379 defaults')
    shell('service redis_6379 start')
