import glob
import importlib
import os
import re
import subprocess
import sys
import urllib

import click
from colorama import Style, Fore


def get_app(app_name):
    app = load_app(app_name)
    if app is None:
        click.echo('ifs does not have a source for "%s"' % app_name)
        exit(1)
    else:
        return app

def error(message=None, nl=True):
    click.echo(Style.BRIGHT + Fore.RED + message + Style.RESET_ALL, sys.stderr, nl)

def ok(message=None, file=None, nl=True):
    click.echo(Style.BRIGHT + Fore.GREEN + message + Style.RESET_ALL, file, nl)

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

def load_app(app_name):
    try:
        mod = importlib.import_module('ifs.source.%s' % app_name, '..source')
    except ImportError as e:
        mod = None
    return mod

def get_download_url(app_name, version=None):
    app = load_app(app_name)
    if not version:
        version = app.version
    return app.download_url.replace('VERSION', version)

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

def app_info(app_name):
    app = load_app(app_name)
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

def install(app_name, version=None, force=False):
    app = load_app(app_name)
    if not version:
        version = app.version
    if check_version(app) == version:
        return '%s %s is already installed' % (app.name, version)
    else:
        # Install dependencies
        deps = Cmd.run(cmd_install_deps(app))
        if deps.returncode > 0:
            return deps

        install = Cmd.run(cmd_install_app(app, version))
        return install
