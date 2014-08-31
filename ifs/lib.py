import glob
import importlib
import os
import re
import subprocess
import sys
import urllib

import click


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


def get_download_url(app, version=None):
    if not version:
        version = app.version
    if hasattr(app, 'download_url') and app.download_url:
        return app.download_url.replace('VERSION', version)
    else:
        return None

def get_download_filename(url, target):
    if url and os.path.isdir(target):
        target += '/' + url.split('/')[-1]
    return None

def download(url, target):
    """
    Target should be an absolute path to the location you want to download the
    file.
    """
    # Add progress bar via:
    # http://stackoverflow.com/a/22776/317916
    if not url:
        return None
    urllib.urlretrieve(url, target)
    return target

def list_apps():
    path = os.path.dirname(os.path.realpath(__file__))
    files = glob.glob(path + '/source/*.py')
    results = []
    for f in files:
        i = os.path.basename(f).split('.')[0]
        if i not in ['__init__']:
            results.append(i)
    return results

def load_app(app_name):
    try:
        mod = importlib.import_module('ifs.source.%s' % app_name, '..source')
    except ImportError as e:
        mod = None
    return mod

def match_semver(string):
    return

def check_version(app):
    # Call app.version_cmd to check which version is currently installed
    cmd = Cmd.run(app.version_cmd)
    if hasattr(app, 'version_re'):
        r = re.compile(app.version_re)
    else:
        r = re.compile('(\d+\.\d+\.\d+)')
    matches = r.search(cmd.output)
    if matches is None:
        return None
    else:
        return matches.group(1)

def app_info(app):
    info = {
        "default_version": app.version,
        "current_version": check_version(app) or 'Not Installed',
        "dependencies": app.depends,
        "download_url": app.download_url,
    }
    return info

def cmd_install_deps(app):
    if hasattr(app, 'depends') and app.depends:
        return 'apt-get install -y %s' % ' '.join(app.depends)
    else:
        return None

def cmd_install_app(app, version=None):
    cmd = app.install_script
    if not version:
        version = app.version
    return cmd.replace('VERSION', version)

def install(app, version=None, force=False):
    if not version:
        version = app.version

    # Create temp directory
    target='/tmp/ifs-%s-%s' % (app.__name__[11:], app.version)
    if not os.path.exists(target):
        os.mkdir(target)
    os.chdir(target)

    # Download source
    dl_url = get_download_url(app, version)
    dl_file = get_download_filename(dl_url, target)
    if dl_file and not os.path.exists(dl_file):
        click.echo('Downloading %s' % dl_url)
        if download(dl_url, dl_file):
            click.echo('Downloaded %s' % dl_url)

    # Install dependencies
    depc = cmd_install_deps(app)
    if depc:
        click.echo('Installing dependencies: %s' % depc)
        deps = Cmd.run(depc)
        if deps.returncode > 0:
            return deps

    click.echo('Installing from source')
    install = Cmd.run(cmd_install_app(app, version))
    return install
