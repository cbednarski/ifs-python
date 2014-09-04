import sys
from textwrap import TextWrapper, dedent

import click
from colorama import Style, Fore

import lib


def get_app(app_name):
    app = lib.App.load(app_name)
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
    """
    List available sources.
    """
    for app in lib.list_app_names():
        click.echo(app)


@cli.command()
@click.argument('term')
def grep(term):
    """
    Search in source name and description.
    """
    apps = lib.search_app_strings(term)
    text = TextWrapper(initial_indent='  ', subsequent_indent='  ')
    for app in apps:
        click.echo(app.name)
        if app.description:
            des = dedent(app.description)
            click.echo(text.fill(app.description))


@cli.command()
@click.argument('app_name')
@click.option('--version')
@click.option('--force', '-f', default=False, is_flag=True)
def install(app_name, version, force):
    """
    Install the specified application.

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
    if app.check_version() == version and not force:
        click.echo('%s %s is already installed' % (app.name, version))
        exit(0)

    cmd = app.install()
    if cmd.returncode == 0:
        ok(cmd.output)
    else:
        error(cmd.output)
    exit(cmd.returncode)


@cli.command()
@click.argument('app_name')
def version(app_name):
    """
    Show the installed source version.

    Abstracts away application-specific flags like -v -V --version -version etc.

    Example: ifs version nginx
    """
    app = get_app(app_name)

    version = app.check_version()
    if version is None:
        error('%s is not installed' % app_name)
        exit(1)

    click.echo(version)


@cli.command()
@click.argument('app_name')
def info(app_name):
    """
    Show source name, version, and deps.
    Run `ifs ls` for a list of applications
    """
    app = get_app(app_name)
    info = app.info()
    for k, v in info.iteritems():
        if type(v) is list:
            v = ' '.join(v)
        click.echo('%s: %s' % (k, v))


if __name__ == '__main__':
    cli()
