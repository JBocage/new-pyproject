def write_package_paths(data_dir: bool = False, models_dir: bool = False):
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

    write_line('    TEST = ROOT / "tests"')

    return file_content
