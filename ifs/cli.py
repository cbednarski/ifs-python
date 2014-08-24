import sys

import click

from lib import *

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
    for app in list_apps():
        click.echo(app)


@cli.command()
@click.argument('term')
def search(term):
    for app in list_apps():
        if term in app:
            click.echo(app)


@cli.command()
@click.argument('app_name')
def install(app_name):
    app = get_app(app_name)
    cmd = install(app_name)
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

    version = check_version(app)
    if version is None:
        error('%s is not installed' % app_name)
        exit(1)

    click.echo(version)


@cli.command()
@click.argument('app_name')
def info(app_name):
    """
    Show information about an app_name from ifs ls
    """
    app = get_app(app_name)
    info = app_info(app_name)
    for k, v in info.iteritems():
        if type(v) is list:
            v = ' '.join(v)
        click.echo('%s: %s' % (k, v))


if __name__ == '__main__':
    cli()
