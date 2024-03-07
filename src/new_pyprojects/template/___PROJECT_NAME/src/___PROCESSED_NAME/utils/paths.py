import pathlib


class Paths:

    ROOT = pathlib.Path(__file__).parent.parent.parent.parent
    SRC = ROOT / "src"

    CLI = SRC / "___PROCESSED_NAME" / "cli"  # F:CLI
    API = SRC / "___PROCESSED_NAME" / "api"  # F:API
    STREAMLIT_APP = SRC / "___PROCESSED_NAME" / "streamlit_app"  # F:STREAMLIT
