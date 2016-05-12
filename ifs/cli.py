import sys
import datetime
from textwrap import TextWrapper, dedent

import click
from colorama import Style, Fore
B = Style.BRIGHT
N = Style.NORMAL

from ifs import lib


def get_app(app_name):
    app = lib.App.load(app_name)
    if app is None:
        click.echo('ifs does not have a source for "%s"' % app_name)
        exit(1)
    else:
        return app


def error(message=None, nl=True):
    click.echo(Style.BRIGHT + Fore.RED + message + Style.RESET_ALL, sys.stderr,
               nl)


def ok(message=None, file=None, nl=True):
    click.echo(Style.BRIGHT + Fore.GREEN + message + Style.RESET_ALL, file, nl)


@click.group()
@click.version_option()
def cli():
    """
    Install From Source

    When the version in the package manager has gone stale, get a fresh,
    production-ready version from a source tarball or precompiled archive.

    Each installation script is called a `source`, identified by a name like
    `nginx`. ifs commands generally operate on these sources e.g. `ifs install
    nginx` or `ifs export nginx`.

    For a list of commands type `ifs ls`. For additional help on any command
    type `ifs COMMAND --help`, e.g. `ifs install --help`.

    Please send issues or improvements to https://github.com/cbednarski/ifs
    """
    pass


@cli.command()
def ls():
    """
    List available sources.

      ifs ls
    """
    for app in lib.list_app_names():
        click.echo(app)


@cli.command()
@click.argument('term')
def grep(term):
    """
    Search in source name and description.

      ifs search nginx
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
@click.option('--version', help='Override the default version')
@click.option('--force', '-f',
              default=False,
              is_flag=True,
              help='Force redownload and reinstall')
def install(app_name, version, force):
    """
    Install the specified application.

      ifs install -f --version 1.6.2 nginx

    To inspect an install script before you run it, use `ifs export SOURCE`.

    Versions

    Sources come in three varieties: compiled packages, source packages,
    and repositories. If a source uses a package (tarball, .deb) the install
    script will be locked to a version. You can override it with --version

      ifs install redis --version 2.8.13

    In this case, if you want to upgrade to a new version you can generally
    just specify the latest version when it comes out, e.g.

      ifs install redis --version 2.8.15

    In the third case packages are installed from an apt repo. By default, ifs
    will install the latest version from the repo when you run install. If you
    want to upgrade later, you can pass -f, e.g. `ifs install -f jenkins`. This
    will force ifs to reinstall the latest (essentially upgrading).

    Upstream Patches

    We strive to provide installers for the latest and greatest versions.

    Sometimes the installation dependencies will change and you'll need to
    modify the installer to get the latest version to install. Please submit a
    patch if you fix something! https://github.com/cbednarski/ifs

    Future-proofing Installations

    There are a slew of variables involved in installing packages, including
    updates to dependencies, security fixes, and so forth.

    If you want to guarantee that the version you install doesn't change over
    time, you should probably use a tool like docker. However, you can achieve
    some naive version-locking by using `ifs export SOURCE` for each app you
    install, and checking these files into your version control. When you
    install later, use `ifs source FILENAME` instead of `ifs install SOURCE`.
    """
    if app_name == 'template':
        click.echo("`template` isn't really an app. It's a dummy that helps "
                   "you create a new ifs installer. Try:\n  ifs export "
                   "template")
        exit(1)

    app = get_app(app_name)
    installed_version = app.check_version()

    if not version:
        version = app.version
    if version and installed_version == version and not force:
        click.echo('%s %s is already installed' %
                   (app.name, installed_version))
        exit(0)
    if installed_version and not version and not force:
        click.echo('%s %s is already installed' %
                   (app.name, installed_version))
        exit(0)

    cmd = app.install(version)
    if cmd.returncode == 0:
        ok("Successfully installed %s version %s" % (app.name, app.version))
    else:
        error("Error installing %s" % app.name)
    exit(cmd.returncode)


@cli.command()
@click.argument('source', type=click.Path(exists=True))
def source(source):
    """
    Install from a custom source.

      ifs source /path/to/source.py

    ifs ships with some built-in source files. This command allows you to load
    your own, arbitrarily-defined source file at runtime. Think of it as the
    bash source built-in for ifs.

    Note: The source file should be a python file with the same basic structure
    as one of the built-in source files. Run `ifs export template` to create a
    new one.
    """
    app = lib.App.load_external(source)
    if app:
        cmd = app.install()
        if cmd.returncode == 0:
            ok('Installation succeeded')
        else:
            error('Installation failed')
        exit(cmd.returncode)
    else:
        error('Unable to load source from %s' % source)
        exit(1)


@cli.command()
@click.argument('source')
def export(source):
    """
    Export a built-in source.

      ifs export template > newapp.py

    This is useful to see details on how a built-in source is installed, or to
    facilitate creating a new source from a template. You can install exported
    sources with `ifs source FILENAME`.
    """
    source_code = lib.export_source(source)
    if source_code:
        click.echo(source_code)
    else:
        error('No built-in source for %s' % source)
        exit(1)


@cli.command()
@click.argument('app_name')
def version(app_name):
    """
    Show the installed source version.

      ifs version nginx

    Abstracts away application-specific flags like -v, -V, --version, etc.
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

      ifs info nginx

    Run `ifs ls` for a list of applications
    """
    app = get_app(app_name)
    info = app.info()
    for k, v in info.iteritems():
        if type(v) is list:
            v = ' '.join(v)
        click.echo('%s: %s' % (k, v))


@cli.command()
@click.option('--force', '-f',
              default=False,
              is_flag=True,
              help='Force update, even if the system was updated recently')
def aptupdate(force):
    """
    Alias for apt-get upgrade and associated housekeeping (clean, autoremove, etc.).
    """
    if force or lib.out_of_date():
        cmd = lib.Cmd.run("""
            apt-get clean
            apt-get update -qq
            apt-get upgrade -yq
            apt-get autoremove -y
            """,
                          autoprint=True)
        lib.write_last_updated()
        exit(cmd.returncode)
    else:
        t = datetime.datetime.fromtimestamp(
            lib.read_last_updated()).isoformat()
        click.echo("System was updated at %s, skipping" % t)
    exit(0)


if __name__ == '__main__':
    cli()
