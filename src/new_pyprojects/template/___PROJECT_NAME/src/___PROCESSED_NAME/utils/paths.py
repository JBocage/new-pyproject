import pathlib


class Paths:

    ROOT = pathlib.Path(__file__).parent.parent.parent.parent
    SRC = ROOT / "src"

    CLI = SRC / "___PROJECT_NAME_PROCESSED" / "cli"  # F:CLI
    API = SRC / "___PROJECT_NAME_PROCESSED" / "api"  # F:API
