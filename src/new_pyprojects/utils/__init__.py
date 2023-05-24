import pathlib


class PackagePaths:
    """Contains useful path for the package"""

    ROOT = pathlib.Path(__file__).resolve().parents[3].absolute()

    TEST = ROOT / "tests"

    UTILS = pathlib.Path(__file__).resolve().parent.absolute()
    PACKAGE_ROOT = UTILS.parent

    TEMPLATES = PACKAGE_ROOT / "templates"
