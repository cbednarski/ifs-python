import click

import lib

def get_app(app_name):
    app = lib.load_app(app_name)
    if app is None:
        click.echo('ifs does not have a source for "%s"' % app_name)
        exit(1)
    else:
        return app


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
def install(app_name):
    app = get_app(app_name)
    cmd = lib.install(app_name)
    click.echo(cmd.output)
    exit(cmd.returncode)


@cli.command()
@click.argument('app_name')
def version(app_name):
    app = get_app(app_name)
    if not app:
        click.echo('ifs does not have a source for "%s"' % app_name)
        exit(1)

    version = lib.check_version(app)
    click.echo(version)
    if version is None:
        exit(1)


@cli.command()
@click.argument('app_name')
def info(app_name):
    """
    Show information about an app_name from ifs ls
    """
    app = get_app(app_name)
    info = lib.app_info(app_name)
    for k, v in info.iteritems():
        if type(v) is list:
            v = ' '.join(v)
        click.echo('%s: %s' % (k, v))


if __name__ == '__main__':
    cli()
