import pathlib


class Paths:
    """A class to store the paths of the project.

    Every path is a :class:`pathlib.Path` object.
    They dynamically update themselves when the project is moved.

    Example usage:

    .. code-block:: python

        from src.tmp.utils.paths import Paths

        print(Paths.ROOT)
    """

    #: The root directory of the project.
    ROOT = pathlib.Path(__file__).parent.parent.parent.parent
    #: The source directory of the project.
    #: This is where the source code of the project is stored.
    SRC = ROOT / "src"

    #: The docs directory for sphinx  # F:DOCS
    DOCS = ROOT / "docs"  # F:DOCS

    #: The CLI directory of the project. This is where the CLI scripts are stored. # F:CLI
    CLI = SRC / "___PROCESSED_NAME" / "cli"  # F:CLI
    #: The API directory of the project. This is where the API scripts are stored. # F:API
    API = SRC / "___PROCESSED_NAME" / "api"  # F:API
    #: The Streamlit app directory of the project.   # F:STREAMLIT
    #: This is where the Streamlit app scripts are stored. # F:STREAMLIT
    STREAMLIT_APP = SRC / "___PROCESSED_NAME" / "streamlit_app"  # F:STREAMLIT
    #: The .env file of the project. # F:ENV
    ENV = ROOT / ".env"  # F:ENV
