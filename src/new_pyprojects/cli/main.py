"""
Implements the command line interface for new-pyprojects

Learn more by running

`new-pyproject --help`
"""

import os
import pathlib
import shutil
from tempfile import TemporaryDirectory

import click

from new_pyprojects.utils.paths import Paths
from new_pyprojects.utils.recursive_copy_and_modify import recurse_copy_and_modify

from .. import __VERSION__

DEFAULT_FIRST_COMMIT_MSG = "Initial commit"
DEFAULT_DESCRIPTION = "A new Python project"


class Config(object):
    """An object designed to conatin and pass the config"""

    def __init__(self) -> None:
        self.config = {}

    def set_config(self, key, value):
        """Sets a key-value pair into the config"""
        self.config[key] = value


@click.command()
@click.version_option(version=__VERSION__)
@click.option(
    "-a",
    "--author-name",
    "author_name",
    type=click.STRING,
    default="",
    help="The name of the author of the project",
)
@click.option(
    "--api",
    "api",
    is_flag=True,
    help="Create an API directory",
)
@click.option(
    "--author-email",
    "author_email",
    type=click.STRING,
    default="",
    help="The email of the author of the project",
)
@click.option(
    "--cli",
    "cli",
    is_flag=True,
    help="Create a CLI directory",
)
@click.option(
    "--cli-name",
    "cli_name",
    type=click.STRING,
    help="The name of the CLI",
)
@click.option(
    "--cli-group",
    "cli_group",
    is_flag=True,
    help="Create a CLI group",
)
@click.option(
    "--description",
    "description",
    type=click.STRING,
    help="The description of the project",
)
@click.option(
    "--no-tests",
    "no_tests",
    is_flag=True,
    help="Do not create a tests directory",
)
@click.option(
    "--no-git",
    "no_git",
    is_flag=True,
    help="Do not create a git repository",
)
@click.option(
    "--first-commit-msg",
    "first_commit_msg",
    type=click.STRING,
    help="The message for the first commit",
)
@click.option(
    "--first-commit",
    "first_commit",
    is_flag=True,
    help="Create the first commit",
)
@click.option(
    "--install",
    "install",
    is_flag=True,
    help="Install the project after creating it",
)
@click.argument("project_name", type=click.STRING, required=True)
@click.pass_context
def cli(ctx, *args, **kwargs):
    """Runs the project-creating command"""
    ctx.obj = Config()
    for key, value in kwargs.items():
        ctx.obj.set_config(key, value)

    names_mapping = {
        "___AUTHOR_NAME": ctx.obj.config["author_name"],
        "___AUTHOR_EMAIL": ctx.obj.config["author_email"],
        "___PROJECT_NAME": ctx.obj.config["project_name"],
        "___PROCESSED_NAME": ctx.obj.config["project_name"].replace("-", "_"),
        "___CLI_NAME": ctx.obj.config["cli_name"] or ctx.obj.config["project_name"],
        "___FIRST_COMMIT_MSG": ctx.obj.config["first_commit_msg"]
        or DEFAULT_FIRST_COMMIT_MSG,
        "___DESCRIPTION": ctx.obj.config["description"] or DEFAULT_DESCRIPTION,
    }

    flags = {
        "API": ctx.obj.config["api"],
        "AUTHOR": bool(ctx.obj.config["author_name"]),
        "AUTHOREMAIL": bool(ctx.obj.config["author_email"]),
        "CLI": bool(
            ctx.obj.config["cli"]
            or ctx.obj.config["cli_name"]
            or ctx.obj.config["cli_group"]
        ),
        "CLIGROUP": ctx.obj.config["cli_group"],
        "CLICOMMAND": not ctx.obj.config["cli_group"],
        "GIT": not ctx.obj.config["no_git"],
        "FIRSTCOMMIT": bool(
            ctx.obj.config["first_commit"] or ctx.obj.config["first_commit_msg"]
        ),
        "INSTALL": ctx.obj.config["install"],
        "TESTS": not ctx.obj.config["no_tests"],
    }

    dst = pathlib.Path.cwd() / ctx.obj.config["project_name"]
    dst.mkdir()

    recurse_copy_and_modify(
        src=Paths.TEMPLATE / "___PROJECT_NAME",
        dst=dst,
        names_to_change=names_mapping,
        flags=flags,
    )

    if ctx.obj.config["install"]:
        os.chdir(str(dst.absolute()))
        os.system("bash " + str(dst.absolute() / "install.sh"))

        # Delete install script
        (dst / "install.sh").unlink()
