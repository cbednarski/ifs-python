import sys

import click
from colorama import Style, Fore

import lib


def get_app(app_name):
    app = lib.load_app(app_name)
    if app is None:
        click.echo('ifs does not have a source for "%s"' % app_name)
        exit(1)
    else:
        return app

def error(message=None, nl=True):
    click.echo(Style.BRIGHT + Fore.RED + message + Style.RESET_ALL, sys.stderr, nl)

def ok(message=None, file=None, nl=True):
    click.echo(Style.BRIGHT + Fore.GREEN + message + Style.RESET_ALL, file, nl)


@click.group()
def cli():
    """
    Install From Source

    When the version in the package manager has gone stale, get a fresh,
    production-ready version from a source tarball or precompiled archive.

    Send issues or improvements to https://github.com/cbednarski/ifs
    """
    pass


@cli.command()
def ls():
    for app in lib.list_apps():
        click.echo(app)


@cli.command()
@click.argument('term')
def search(term):
    for app in lib.list_apps():
        if term in app:
            click.echo(app)


@cli.command()
@click.argument('app_name')
@click.option('--version')
@click.option('--force', '-f', default=False, is_flag=True)
def install(app_name, version, force):
    """
    Install the specified application

    --version 1.0.0: override the default version as indicated in ifs info
    -f --force: purge cached downloads and source files and reinstall

    Note that overriding the version is not guaranteed to work, as the build
    script itself may change between versions. However, this should allow you
    to do minor upgrades and some naive version pinning idependently of ifs
    source versions.
    """
    app = get_app(app_name)

    if not version:
        version = app.version
    if lib.check_version(app) == version and not force:
        click.echo('%s %s is already installed' % (app.__name__[11:], version))
        exit(0)

    cmd = lib.install(app)
    if cmd.returncode == 0:
        ok(cmd.output)
    else:
        error(cmd.output)
    exit(cmd.returncode)


@cli.command()
@click.argument('app_name')
def version(app_name):
    app = get_app(app_name)
    if not app:
        error('ifs does not have a source for "%s"' % app_name)
        exit(1)

    version = lib.check_version(app)
    if version is None:
        error('%s is not installed' % app_name)
        exit(1)

    click.echo(version)


@cli.command()
@click.argument('app_name')
def info(app_name):
    """
    Show information about an application source
    Run `ifs ls` for a list of applications
    """
    app = get_app(app_name)
    info = lib.app_info(app)
    for k, v in info.iteritems():
        if type(v) is list:
            v = ' '.join(v)
        click.echo('%s: %s' % (k, v))


if __name__ == '__main__':
    cli()
