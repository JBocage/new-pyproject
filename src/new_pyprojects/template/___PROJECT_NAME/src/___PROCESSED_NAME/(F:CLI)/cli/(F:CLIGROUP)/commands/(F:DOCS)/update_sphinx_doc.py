import os

import click
from ___PROCESSED_NAME.utils.paths import Paths


@click.group("doc")
@click.pass_context
def doc_cli_group(ctx, *args, **kwargs):
    """
    A group of commands to manage the documentation
    """
    pass


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

    os.chdir(str(Paths.ROOT))
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
