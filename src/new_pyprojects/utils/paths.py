import pathlib


class Paths:

    ROOT = pathlib.Path(__file__).parent.parent.parent.parent

    SRC = ROOT / "src"

    templates = SRC / "new_pyprojects" / "template"
