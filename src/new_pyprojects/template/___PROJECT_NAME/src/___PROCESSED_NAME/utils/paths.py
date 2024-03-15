import pathlib


class Paths:
    """A class to store the paths of the project.

    Every path is a :class:`pathlib.Path` object.
    They dynamically update themselves when the project is moved.

    Example usage:

    .. code-block:: python

        from ___PROCESSED_NAME.utils.paths import Paths

        print(Paths.ROOT)
    """

    #: The root directory of the package.
    PACKAGE_ROOT = pathlib.Path(__file__).parent.parent
    #: The source directory of the project.
    #: This is where the source code of the project is stored.
    #: WARNING: This is not the root directory of the project and using this
    #: may cause issues if the project is installed as a package.
    SRC = PACKAGE_ROOT.parent
    #: The root directory of the project.
    #: WARNING: This is not the root directory of the project and using this
    #: may cause issues if the project is installed as a package.
    ROOT = SRC.parent

    #: The docs directory for sphinx  # F:DOCS
    DOCS = ROOT / "docs"  # F:DOCS

    #: The CLI directory of the project. This is where the CLI scripts are stored. # F:CLI
    CLI = PACKAGE_ROOT / "cli"  # F:CLI
    #: The API directory of the project. This is where the API scripts are stored. # F:API
    API = PACKAGE_ROOT / "api"  # F:API
    #: The Streamlit app directory of the project.   # F:STREAMLIT
    #: This is where the Streamlit app scripts are stored. # F:STREAMLIT
    STREAMLIT_APP = PACKAGE_ROOT / "streamlit_app"  # F:STREAMLIT
