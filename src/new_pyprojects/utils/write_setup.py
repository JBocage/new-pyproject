"""Implement a setup.py writing function"""
from typing import Optional


def write_setup(
    project_name: str,
    author: Optional[str] = None,
    author_email: Optional[str] = None,
    cli_entrypoint: Optional[str] = None,
    cli_in_src: bool = False,
):
    """Generates the content for a setup.py files.

    Args:
        project_name (str): The name of the package
        author (Optional[str], optional): The author of the package.
            Defaults to None.
        author_email (Optional[str], optional):The author email of the package.
            Defaults to None.
        cli_entrypoint (Optional[str], optional): If provided, will add
            a cli entrypoint to the package. It will be spelled like
            the provided string. Defaults to None.
        cli_in_src (bool, optional): Whether to put cli-related scripts in src,
            along with the package actual code. Defaults to False.
    """

    setup_file_content = ""

    def add_line(line: str = ""):
        """Adds a line to the setup file content"""
        nonlocal setup_file_content
        setup_file_content += line + "\n"

    add_line("import pathlib")
    add_line()
    add_line("from setuptools import find_packages, setup")
    add_line()
    add_line(
        f"from src.{project_name} import __DESCRIPTION__, __PACKAGE_NAME__, __VERSION__"
    )
    for line in """here = pathlib.Path(__file__).parent.resolve()

# Get the long description from the README file
long_description = (here / "README.md").read_text(encoding="utf-8")

with open(here / "requirements.txt", "r") as requirements_file:
    install_requires = [
        requirement.strip()
        for requirement in requirements_file.readlines()
        if (requirement.strip() and requirement.strip()[:1] != "#")
    ]


setup(
    name=__PACKAGE_NAME__,
    version=".".join([str(v) for v in __VERSION__]),
    description=__DESCRIPTION__,
    long_description=long_description,
    long_description_content_type="text/markdown",""".split(
        "\n"
    ):
        add_line(line)

    if author:
        add_line(f'    author="{author}",')
    if author_email:
        add_line(f'    author_email="{author_email}",')

    for line in """    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "Programming Language :: Python :: 3.8",
    ],
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.7, <4",
    install_requires=install_requires,""".split(
        "\n"
    ):
        add_line(line)

    if cli_entrypoint:
        if cli_in_src:
            add_line(
                '    entry_points={"console_scripts": ["'
                + cli_entrypoint
                + " = "
                + project_name
                + '_cli.main:cli"]},'
            )
        else:
            add_line(
                '    entry_points={"console_scripts": ["'
                + cli_entrypoint
                + " = "
                + project_name
                + '.cli.main:cli"]},'
            )

    add_line(")")

    return setup_file_content
