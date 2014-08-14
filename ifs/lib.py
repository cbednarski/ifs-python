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

def list_apps():
    path = os.path.dirname(os.path.realpath(__file__))
    files = glob.glob(path + '/source/*.py')
    results = []
    for f in files:
        i = os.path.basename(f).split('.')[0]
        if i not in ['__init__']:
            results.append(i)
    return results

def load_app(application):
    return importlib.import_module('ifs.source.nginx', '..source')

def get_download_url(application, version=None):
    app = load_app(application)
    if not version:
        version = app.version
    return app.download_url.replace('VERSION', version)

def check_version(application):
    # Call app.version_cmd to check which version is currently installed
    return None

def app_info(application):
    app = load_app(application)
    info = {
        "default_version": app.version,
        "current_version": check_version(application) or 'Not Installed',
        "dependencies": app.depends,
        "download_url": app.download_url,
    }
    return info

def install(application, version=None, force=False):
    app = load_app(application)
    if not version:
        version = app.version
    installed_version = bash(app.version_cmd)
    if installed_version:
        pass
    else:
        pass
