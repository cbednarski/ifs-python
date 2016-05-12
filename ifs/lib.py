import glob
import imp
import importlib
import os
import re
import subprocess
import time
import sys
if sys.version_info[0] == 2:
    from urllib import urlretrieve
else:
    from urllib.request import urlretrieve


import click


# We want this to persist across reboots so do not use /tmp
last_updated_file = '/var/lib/ifs/last_update'


def get_download_filename(url, target):
    """
    Given a URL and a path on the filesystem that may be a directory or file,
    return the filename that we will save our download into.

    E.g: http://blah/file.tar, /tmp -------------> /tmp/file.tar
    And: http://blah/file.tar, /tmp/archive.tar -> /tmp/archive.tar
    """
    if url and os.path.isdir(target):
        target += '/' + url.split('/')[-1]
        return target
    return None


def download(url, target):
    """
    Download URL to TARGET on your local filesystem. TARGET should be an
    absolute path to the location you want to download the file. Useful when
    curl / wget are not installed, but python is.
    """
    # Add progress bar via:
    # http://stackoverflow.com/a/22776/317916
    if not url:
        return None
    urlretrieve(url, target)
    return target


def list_app_names():
    path = os.path.dirname(os.path.realpath(__file__))
    files = glob.glob(path + '/source/*.py')
    results = []
    for f in files:
        i = os.path.basename(f).split('.')[0]
        if i not in ['__init__']:
            results.append(i)
    results.sort()
    return results


def list_apps():
    apps = []
    for app_name in list_app_names():
        apps.append(App.load(app_name))
    return apps


def search_app_strings(term):
    results = set()
    for app in list_apps():
        if app.name and term in app.name:
            results.add(app)
        if app.description and term in app.description:
            results.add(app)
    return results


def export_source(source):
    path = os.path.dirname(os.path.realpath(__file__))
    source_file = path + '/source/%s.py' % source
    if os.path.exists(source_file):
        return open(source_file).read()
    else:
        return None


def match_semver(string):
    return


def read_last_updated():
    if os.path.exists(last_updated_file):
        with open(last_updated_file) as f:
            try:
                return int(float(f.read()))
            except ValueError:
                return 0
    return 0


def write_last_updated():
    path = os.path.dirname(last_updated_file)
    if not os.path.isdir(path):
        os.makedirs(path, 0o755)
    with open(last_updated_file, 'w') as f:
        f.write(str(time.time()))
        f.close()


def out_of_date(delay=86400):
    t = time.time()
    if t - read_last_updated() > delay:
        return True
    return False


class Cmd(object):
    returncode = None
    cmd = None
    output = None

    def __init__(self, cmd):
        cmd = "set -e\n%s" % cmd
        self.cmd = cmd

    def execute(self, autoprint=False):
        p = subprocess.Popen(self.cmd,
                             stdout=subprocess.PIPE,
                             stderr=subprocess.STDOUT,
                             bufsize=1,
                             shell=True)
        output = ''
        for line in iter(p.stdout.readline, b''):
            sline = line.decode(sys.stdout.encoding)
            output += sline
            if autoprint:
                print(sline, end='')
        p.communicate()
        self.output = output
        self.returncode = p.returncode
        return self.returncode == 0

    @classmethod
    def run(cls, cmd, autoprint=False):
        cmdo = cls(cmd)
        cmdo.execute(autoprint)
        return cmdo


class App(object):
    depends = None
    description = None
    download_url = None
    install_script = None
    name = None
    version = None
    version_cmd = None

    def __init__(self, name, module=None):
        self.name = name
        if module:
            for k, v in module.__dict__.items():
                if k[0] != '_':
                    setattr(self, k, v)
        # self.__dict__.update(module.__dict__)

    @classmethod
    def load(cls, app_name):
        try:
            mod = importlib.import_module('ifs.source.%s' % app_name,
                                          '..source')
            app = cls(app_name, mod)
        except ImportError:
            app = None
        return app

    @classmethod
    def load_external(cls, path):
        d, f = os.path.split(path)
        name, ext = os.path.splitext(f)
        try:
            module = imp.load_source(name, path)
            app = cls(name, module)
            return app
        except Exception:
            return None

    def get_download_url(self, version=None):
        if not version:
            version = self.version
        if hasattr(self, 'download_url') and self.download_url:
            return self.download_url.replace('VERSION', version)
        else:
            return None

    def check_version(self):
        # Call self.version_cmd to check which version is currently installed
        cmd = Cmd.run(self.version_cmd)
        if hasattr(self, 'version_re'):
            r = re.compile(self.version_re)
        else:
            r = re.compile('(\d+\.\d+\.\d+)')
        matches = r.search(cmd.output)
        if matches is None:
            return None
        else:
            return matches.group(1)

    def info(self):
        info = {
            "description": self.description or self.name,
            "default_version": self.version or None,
            "current_version": self.check_version() or 'Not Installed',
            "dependencies": self.depends or None,
            "download_url": self.download_url or None,
        }
        return info

    def cmd_install_deps(self):
        if hasattr(self, 'depends') and self.depends:
            return 'apt-get install -y %s' % ' '.join(self.depends)
        else:
            return None

    def cmd_install_app(self, version=None):
        cmd = self.install_script
        if not version:
            version = self.version
        if version:
            cmd = cmd.replace('VERSION', version)
        return cmd

    def install(self, version=None):
        if not version:
            version = self.version

        # Create temp directory
        target = '/tmp/ifs-%s-%s' % (self.name, version)
        if not os.path.exists(target):
            os.mkdir(target)
        os.chdir(target)

        # Download source
        dl_url = self.get_download_url(version)
        dl_file = get_download_filename(dl_url, target)
        if dl_file:
            if os.path.exists(dl_file):
                click.echo('Already downloaded %s' % dl_file)
            else:
                click.echo('Downloading %s to %s' % (dl_url, dl_file))
                if download(dl_url, dl_file):
                    click.echo('Download complete')

        # Install dependencies
        depc = self.cmd_install_deps()
        if depc:
            click.echo('Installing dependencies: %s' % depc)
            deps = Cmd.run(depc)
            if deps.returncode > 0:
                return deps

        click.echo('Installing from source')
        install = Cmd.run(self.cmd_install_app(version), True)
        return install
