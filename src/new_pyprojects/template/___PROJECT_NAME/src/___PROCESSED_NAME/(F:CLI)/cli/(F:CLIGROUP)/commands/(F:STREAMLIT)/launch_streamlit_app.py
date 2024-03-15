import os

import click
from ___PROCESSED_NAME.utils.paths import Paths


@click.command("launch-streamlit")
@click.pass_context
def launch_streamlit_app(ctx, *args, **kwargs):
    """
    Launches the streamlit app
    """

    os.system(f"streamlit run {str(Paths.STREAMLIT_APP / 'main.py')}")
