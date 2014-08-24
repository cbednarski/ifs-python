import glob
import os
import subprocess
import urllib
import importlib

from source import nginx

class Cmd(object):
    returncode = None
    cmd = None
    output = None

    def __init__(self, cmd):
        cmd = "set -e\n%s" % cmd
        self.cmd = cmd

    def execute(self):
        try:
            self.output = subprocess.check_output(self.cmd, stderr=subprocess.STDOUT, shell=True)
            self.returncode = 0
            return True
        except subprocess.CalledProcessError as e:
            self.output = e.output
            self.returncode = e.returncode
            return False

    @classmethod
    def run(cls, cmd):
        cmdo = cls(cmd)
        cmdo.execute()
        return cmdo


def download(url, filename):
    # Add progress bar via:
    # http://stackoverflow.com/a/22776/317916
    urllib.urlretrieve(url, filename)

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
    try:
        mod = importlib.import_module('ifs.source.%s' % application, '..source')
    except ImportError as e:
        mod = None
    return mod

def get_download_url(application, version=None):
    app = load_app(application)
    if not version:
        version = app.version
    return app.download_url.replace('VERSION', version)

def match_semver(string):
    return

def check_version(application):
    # Call app.version_cmd to check which version is currently installed
    cmd = Cmd.run(application.version_cmd)
    return cmd.output

def app_info(application):
    app = load_app(application)
    info = {
        "default_version": app.version,
        "current_version": check_version(app) or 'Not Installed',
        "dependencies": app.depends,
        "download_url": app.download_url,
    }
    return info

def install_deps(application):
    if application.depends:
        return 'apt-get install -y %s' % ' '.join(application.depends)
    else:
        return False

def install_app(application, version=None):
    cmd = application.install_script
    if not version:
        version = application.version
    return cmd.replace('VERSION', version)

def install(application, version=None, force=False):
    app = load_app(application)
    if not version:
        version = app.version
    if check_version(app) == version:
        return '%s %s is already installed' % (app.name, version)
    else:
        # Install dependencies
        deps = Cmd.run(install_deps(app))
        if deps.returncode > 0:
            return deps

        install = Cmd.run(install_app(app, version))
        return install
