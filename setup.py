"""The setup file for the project
"""

import pathlib

from setuptools import find_packages, setup

from src.new_pyprojects import __DESCRIPTION__, __PACKAGE_NAME__, __VERSION__

here = pathlib.Path(__file__).parent.resolve()

# Get the long description from the README file
long_description = (here / "README.md").read_text(encoding="utf-8")

# Get the requirements
install_requires = [
    requirement
    for requirement in (here / "requirements.txt")
    .read_text(encoding="utf-8")
    .split("\n")
    if (requirement.strip() and requirement.strip()[:1] != "#")
]

# __VERSION__ = (0, 0, 1)
# __PACKAGE_NAME__ = "package_name"
# __DESCRIPTION__ = "package description"


setup(
    name=__PACKAGE_NAME__,
    version=".".join([str(v) for v in __VERSION__]),
    description=__DESCRIPTION__,
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="J. Bocage",
    author_email="julien.bocage@gmail.com",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "Programming Language :: Python :: 3.8",
    ],
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.7, <4",
    # This field lists other packages that your project depends on to run.
    # Any package you put here will be installed by pip when your project is
    # installed, so they must be valid existing projects.
    #
    # For an analysis of "install_requires" vs pip's requirements files see:
    # https://packaging.python.org/discussions/install-requires-vs-requirements/
    install_requires=install_requires,  # Optional
    # If there are data files included in your packages that need to be
    # installed, specify them here.
    include_package_data=True,
    # Although 'package_data' is the preferred approach, in some case you may
    # need to place data files outside of your packages. See:
    # http://docs.python.org/distutils/setupscript.html#installing-additional-files
    #
    # In this case, 'data_file' will be installed into '<sys.prefix>/data'
    entry_points={"console_scripts": ["new-pyproject = new_pyprojects.cli.main:cli"]},
)
