from ifs import lib

class Object(object):
    pass

def test_list_apps():
    apps = lib.list_apps()
    assert 'nginx' in apps
    assert '__init__' not in apps

def test_load_app():
    app = lib.load_app('nginx')
    assert app.download_url == 'http://nginx.org/download/nginx-VERSION.tar.gz'

    app = lib.load_app('candycorn')
    assert app is None

def test_get_download_url():
    url = lib.get_download_url(lib.load_app('nginx'))
    assert url == 'http://nginx.org/download/nginx-1.6.1.tar.gz'

    url = lib.get_download_url(lib.load_app('nginx'), '1.6.3')
    assert url == 'http://nginx.org/download/nginx-1.6.3.tar.gz'

def test_app_info():
    info = lib.app_info(lib.load_app('nginx'))
    assert 'default_version' in info
    assert info['download_url'] == 'http://nginx.org/download/nginx-VERSION.tar.gz'

def test_check_version():
    app = Object()
    app.version_cmd = 'venv/bin/py.test --version'
    assert lib.check_version(app) == '2.6.1'

    app.version_re = 'pytest version (\d+\.\d+\.\d+)'
    assert lib.check_version(app) == '2.6.1'

    app.version_cmd = 'echo "pie"'
    assert lib.check_version(app) == None

def test_cmd_install_deps():
    app = Object()
    app.version_cmd = 'ls'
    assert lib.cmd_install_deps(app) == None

    app.depends = []
    assert lib.cmd_install_deps(app) == None

    app.depends = ['blah']
    assert lib.cmd_install_deps(app) == 'apt-get install -y blah'

    app.depends = ['blah', 'blee']
    assert lib.cmd_install_deps(app) == 'apt-get install -y blah blee'

def test_cmd_install_app():
    app = Object()
    app.version = '1.2.3'
    app.install_script = 'application-VERSION-blah-VERSION'
    assert lib.cmd_install_app(app) == 'application-1.2.3-blah-1.2.3'