import click


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
    click.echo('list of things')


@cli.command()
def search():
    click.echo('searching...')


@cli.command()
def install():
    click.echo('install!')


if __name__ == '__main__':
    cli()
