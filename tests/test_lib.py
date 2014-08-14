from ifs import lib

def test_list_apps():
    apps = lib.list_apps()
    assert 'nginx' in apps
    assert '__init__' not in apps

