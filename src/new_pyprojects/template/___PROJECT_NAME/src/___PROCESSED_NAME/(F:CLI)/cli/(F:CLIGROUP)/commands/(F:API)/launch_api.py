import os

import click


@click.command("launch-api")
@click.pass_context
def launch_api(ctx, *args, **kwargs):
    """
    Hello world command
    """

    from ___PROCESSED_NAME.utils.paths import Paths

    os.chdir(str(Paths.ROOT))
    os.system("uvicorn src.___PROCESSED_NAME.api.main:app --reload")
