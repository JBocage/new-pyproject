import pathlib


class Paths:

    ROOT = pathlib.Path(__file__).parent.parent.parent.parent

    SRC = ROOT / "src"

    PACKAGE_ROOT = pathlib.Path(__file__).parent.parent

    TEMPLATE = PACKAGE_ROOT / "template"
