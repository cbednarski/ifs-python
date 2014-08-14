import click

import lib


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
def search():
    click.echo('searching...')


@cli.command()
def install():
    click.echo(lib.install('nginx'))


@cli.command()
@click.argument('application')
def info(application):
    """
    Show information about an application from ifs ls
    """
    info = lib.app_info(application)
    for k, v in info.iteritems():
        if type(v) is list:
            v = ' '.join(v)
        click.echo('%s: %s' % (k, v))


if __name__ == '__main__':
    cli()
