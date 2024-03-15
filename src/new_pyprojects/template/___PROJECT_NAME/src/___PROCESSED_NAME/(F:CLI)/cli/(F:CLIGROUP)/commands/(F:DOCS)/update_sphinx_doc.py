import os
import shutil

import click
from ___PROCESSED_NAME.utils.paths import Paths


@click.group("doc")
@click.pass_context
def doc_cli_group(ctx, *args, **kwargs):
    """
    A group of commands to manage the documentation
    """
    # Check if the docs directory exists
    sphinx_conf_path = Paths.DOCS / "source" / "conf.py"

    if not sphinx_conf_path.exists():
        print(
            "\nThe docs directory does not exist. You are"
            " probably running this command in a packaged"
            " version of the project.\nTo access this part of the command,"
            " you need to run the command from a cloned version of the project.\n"
        )
        exit(1)


def open_doc():
    # Open the generated documentation
    os.system(f"open {str(Paths.DOCS / 'build' / 'html' / 'index.html')}")


@doc_cli_group.command("update")
@click.pass_context
@click.option(
    "--open",
    "-o",
    "open",
    is_flag=True,
    help="Open the documentation after updating",
)
def update_sphinx_doc(ctx, *args, **kwargs):
    """
    Updates the sphinx doc
    """

    shutil.rmtree(str(Paths.DOCS / "source" / "generated_full_doc"), ignore_errors=True)
    os.system(
        f"sphinx-apidoc -o {str(Paths.DOCS / 'source' / 'generated_full_doc')} "
        f"{str(Paths.SRC / '___PROCESSED_NAME')}"
    )
    os.system(
        f"sphinx-build -M html {str(Paths.DOCS / 'source')} {str(Paths.DOCS / 'build')}"
    )
    if kwargs["open"]:
        open_doc()


@doc_cli_group.command("open")
@click.pass_context
def open_sphinx_doc(ctx, *args, **kwargs):
    """
    Open the sphinx doc
    """
    open_doc()
