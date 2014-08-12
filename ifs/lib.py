import glob
import os
import subprocess
import urllib
import importlib

from source import nginx

def download(url, filename):
    # Add progress bar via:
    # http://stackoverflow.com/a/22776/317916
    urllib.urlretrieve(url, filename)

def bash(command):
    try:
        return subprocess.check_output(command, shell=True)
    except subprocess.CalledProcessError as e:
        return False

def find_apps():
    path = os.path.dirname(os.path.realpath(__file__))
    files = glob.glob(path + '/source/*.py')
    results = []
    for f in files:
        i = os.path.basename(f).split('.')[0]
        if i not in ['__init__']:
            results.append(i)
    return results

def install(application, version=None, force=False):
    app = importlib.import_module('ifs.source.nginx', '..source')
    if not version:
        version = app.version
    installed_version = bash(app.version_cmd)
    if installed_version:
        pass
    else:
        pass

if __name__ == '__main__':
    print find_apps()