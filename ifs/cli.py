import click


@click.group()
def cli():
    pass


@cli.command()
def ls():
    click.echo('list of things')


@cli.command()
def install():
    click.echo('install!')


if __name__ == '__main__':
    cli()
