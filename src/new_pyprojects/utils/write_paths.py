"""Implements a function to initialise dynamic paths"""


def write_package_paths(
    data_dir: bool = False, models_dir: bool = False, tests_dir: bool = True
) -> str:
    """Writes the package paths file. It defines the dynamic paths of the project

    Args:
        data_dir (bool, optional): Whether there is a data directory for
            the project. Defaults to False.
        models_dir (bool, optional): Whether there is a models directory for the
            project. Defaults to False.
        tests_dir (bool, optional): Whether there is a tests directory for the
            project. Defaults to False.

    Returns:
        str: The content of the path-defining py file
    """
    file_content = ""

    def write_line(line: str = ""):
        nonlocal file_content
        file_content += line + "\n"

    write_line("import pathlib")
    write_line()
    write_line()
    write_line("class PackagePaths:")
    write_line('    """Contains useful path for the package"""')
    write_line()
    write_line("    ROOT = pathlib.Path(__file__).resolve().parents[3].absolute()\n")

    if data_dir:
        write_line('    DATA = ROOT / "data"\n')
    if models_dir:
        write_line('    MODELS = ROOT / "models"\n')
    if tests_dir:
        write_line('    TEST = ROOT / "tests"\n')

    return file_content
