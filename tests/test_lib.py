from ifs import lib


def test_list_apps():
    apps = lib.list_apps()
    found = False
    for app in apps:
        if app.name == "nginx":
            found = True
    assert found
    assert '__init__' not in apps


def test_load_app():
    app = lib.App.load('nginx')
    assert app.download_url == 'http://nginx.org/download/nginx-VERSION.tar.gz'

    app = lib.App.load('candycorn')
    assert app is None


def test_get_download_url():
    url = lib.App.load('nginx').get_download_url()
    assert url == 'http://nginx.org/download/nginx-1.10.2.tar.gz'

    url = lib.App.load('nginx').get_download_url('1.6.3')
    assert url == 'http://nginx.org/download/nginx-1.6.3.tar.gz'


def test_app_info():
    info = lib.App.load('nginx').info()
    assert 'default_version' in info
    assert info['download_url'] == 'http://nginx.org/download/nginx-VERSION.tar.gz'


def test_check_version():
    app = lib.App('py.test')
    app.version_cmd = 'venv/bin/py.test --version'
    assert app.check_version() == '2.6.1'

    app.version_re = 'pytest version (\d+\.\d+\.\d+)'
    assert app.check_version() == '2.6.1'

    app.version_cmd = 'echo "pie"'
    assert app.check_version() == None


def test_cmd_install_deps():
    app = lib.App('ls')
    app.version_cmd = 'ls'
    assert app.cmd_install_deps() == None

    app.depends = []
    assert app.cmd_install_deps() == None

    app.depends = ['blah']
    assert app.cmd_install_deps() == 'apt-get install -y blah'

    app.depends = ['blah', 'blee']
    assert app.cmd_install_deps() == 'apt-get install -y blah blee'


def test_cmd_install_app():
    app = lib.App('application')
    app.version = '1.2.3'
    app.install_script = 'application-VERSION-blah-VERSION'
    assert app.cmd_install_app() == 'application-1.2.3-blah-1.2.3'
