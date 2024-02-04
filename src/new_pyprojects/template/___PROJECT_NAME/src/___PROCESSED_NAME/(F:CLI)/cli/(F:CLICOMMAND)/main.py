"""
Implements the command line interface for new-pyprojects

Learn more by running
"""

import click

from .. import __VERSION__


class Config(object):
    """An object designed to conatin and pass the config"""

    def __init__(self) -> None:
        self.config = {}

    def set_config(self, key, value):
        """Sets a key-value pair into the config"""
        self.config[key] = value


@click.command()
@click.version_option(version=__VERSION__)
@click.pass_context
def cli(ctx, *args, **kwargs):
    """Runs the project-creating command"""
    ctx.obj = Config()
    for key, value in kwargs.items():
        ctx.obj.set_config(key, value)

    print("Yo!")
