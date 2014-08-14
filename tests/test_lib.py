from ifs import lib

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
    url = lib.get_download_url('nginx')
    assert url == 'http://nginx.org/download/nginx-1.6.1.tar.gz'

    url = lib.get_download_url('nginx', '1.6.3')
    assert url == 'http://nginx.org/download/nginx-1.6.3.tar.gz'

def test_app_info():
    info = lib.app_info('nginx')
    assert 'default_version' in info
    assert info['download_url'] == 'http://nginx.org/download/nginx-VERSION.tar.gz'
