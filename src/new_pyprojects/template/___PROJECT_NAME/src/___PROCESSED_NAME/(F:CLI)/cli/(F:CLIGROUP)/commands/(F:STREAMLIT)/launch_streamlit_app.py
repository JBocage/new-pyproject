import os

import click
from tmp.utils.paths import Paths


@click.command("launch-streamlit")
@click.pass_context
def launch_streamlit_app(ctx, *args, **kwargs):
    """
    Launches the streamlit app
    """

    os.chdir(str(Paths.ROOT))
    os.system(f"streamlit run {str(Paths.STREAMLIT_APP / 'main.py')}")
