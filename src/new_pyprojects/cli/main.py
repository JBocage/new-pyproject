"""This file implements a command line interface for launching generators"""

import os
import pathlib
import shutil
from typing import Literal, Optional

import click

from new_pyprojects.utils.write_paths import write_package_paths
from new_pyprojects.utils.write_setup import write_setup

from .. import __VERSION__


class Config(object):
    """An object designed to conatin and pass the config"""

    def __init__(self) -> None:
        self.config = {}

    def set_config(self, key, value):
        """Sets a key-value pair into the config"""
        self.config[key] = value


@click.command()
@click.version_option(version=__VERSION__)
@click.option(
    "-a",
    "--author-name",
    "author_name",
    type=click.STRING,
    help="The name of the author of the project",
)
@click.option(
    "--author-email",
    "author_email",
    type=click.STRING,
    help="The email of the author of the project",
)
@click.option(
    "--cli-entrypoint",
    "cli_entrypoint",
    type=click.STRING,
    help="The name of the cli command for the project",
)
@click.option(
    "--cli-in-src",
    "cli_in_src",
    is_flag=True,
    help="Whether to put the cli-related scripts outside of the main project's scripts",
)
@click.option(
    "--cli-type",
    "cli_type",
    type=click.Choice(["group", "command"]),
    help="Whether the cli should be a single command or a command group",
)
@click.option(
    "--data-dir",
    "add_data_dir",
    is_flag=True,
    help="Add a data directory with a gitignore",
)
@click.option(
    "-d",
    "--description",
    "package_description",
    type=click.STRING,
    help="The one line description of the project",
)
@click.option(
    "--fastapi-backend",
    "fastapi_backend",
    is_flag=True,
    help="Adds a fastapi related directory",
)
@click.option(
    "-i",
    "--install",
    "run_install",
    is_flag=True,
    help="Creates a venv and installs once all the files are in",
)
@click.option(
    "-m",
    "--ml-project",
    "is_ml_project",
    is_flag=True,
    help="Whether the project is a machine learning project",
)
@click.option(
    "--no-test",
    "no_test_folder",
    is_flag=True,
    help="Prevents the creation of a test folder",
)
@click.argument("project_name", type=click.STRING, required=True)
@click.pass_context
def cli(ctx, *args, **kwargs):
    """Loads all high level kwargs into the config"""
    ctx.obj = Config()
    for key, value in kwargs.items():
        ctx.obj.set_config(key, value)

    # Parse args
    args = ctx.obj.config
    project_name: str = args["project_name"]
    author_name: Optional[str] = args["author_name"]
    author_email: Optional[str] = args["author_email"]
    add_data_dir: bool = args["add_data_dir"]
    cli_entrypoint: Optional[str] = args["cli_entrypoint"]
    cli_in_src: bool = args["cli_in_src"]
    cli_type: Optional[Literal["group", "command"]] = args["cli_type"]
    fastapi_backend: bool = args["fastapi_backend"]
    is_ml_project: bool = args["is_ml_project"]
    no_test_folder: bool = args["no_test_folder"]
    run_install: bool = args["run_install"]
    package_description: Optional[str] = args["package_description"]

    # Compute args
    package_name = project_name.replace("-", "_")
    add_data_dir = add_data_dir or is_ml_project

    if [cli_entrypoint, cli_type].count(None) == 1:
        raise ValueError(
            "cli-type and cli-entrypoint have to be either both provided"
            f"of both ignored. Got cli-type={cli_type} and cli-entrypoint={cli_entrypoint}"
        )

    from new_pyprojects.utils import PackagePaths

    _call_path = pathlib.Path(os.getcwd()).resolve().absolute()
    project_root = _call_path / project_name

    if project_root.exists():
        raise FileExistsError("You are trying to create a project that already exists")

    # Build ROOT
    project_root.mkdir()

    for fpath in (PackagePaths.TEMPLATES / "root_dir_files").iterdir():
        shutil.copy(fpath, project_root / fpath.name)

    setup_str = write_setup(
        project_name=project_name,
        author=author_name,
        author_email=author_email,
        cli_entrypoint=cli_entrypoint,
        cli_in_src=cli_in_src,
    )

    requirements = []
    if cli_entrypoint:
        requirements.append("click")
    if is_ml_project:
        requirements.extend(
            [
                "torch",
                "matplotlib",
                "joblib",
            ]
        )
    if fastapi_backend:
        requirements.extend(
            [
                "fastapi",
                "pydantic",
            ]
        )
    requirements = sorted(list(set(requirements)))
    print(requirements)
    with open(project_root / "requirements.txt", "w+") as f:
        f.write("\n".join(requirements))

    with open(project_root / "setup.py", "w+") as f:
        f.write(setup_str)

    # Build SRC
    src_path = project_root / "src" / package_name
    src_path.mkdir(parents=True)
    (src_path.parent / "__init__.py").touch()

    with open(src_path / "__init__.py", "w+") as f:
        f.write(
            f"__VERSION__ = (0, 0, 1)\n"
            f'__PACKAGE_NAME__ = "{project_name}"\n'
            f'__DESCRIPTION__ = "{package_description}"\n'
        )

    # Build utils
    utils_path = src_path / "utils"
    utils_path.mkdir()

    with open(utils_path / "__init__.py", "w+") as f:
        f.write("from .paths import PackagePaths")

    with open(utils_path / "paths.py", "w+") as f:
        f.write(
            write_package_paths(
                data_dir=add_data_dir,
                models_dir=is_ml_project,
            )
        )

    # Build cli
    if cli_entrypoint:
        if cli_in_src:
            cli_path = src_path.parent / (project_name + "_cli")
        else:
            cli_path = src_path / "cli"
        cli_path.mkdir()

        (cli_path / "__init__.py").touch()

        if cli_type == "command":
            with open(cli_path / "main.py", "w+") as f:
                f.write(
                    (PackagePaths.TEMPLATES / "cli_dir_files" / "main_command.py")
                    .read_text()
                    .replace("PACKAGE_NAME", package_name)
                )
        else:
            with open(cli_path / "main.py", "w+") as f:
                f.write(
                    (PackagePaths.TEMPLATES / "cli_dir_files" / "main_group.py")
                    .read_text()
                    .replace("PACKAGE_NAME", package_name)
                )
            commands_path = cli_path / "commands"
            commands_path.mkdir()
            shutil.copy(
                PackagePaths.TEMPLATES / "cli_dir_files" / "other_command_group.py",
                commands_path / "hello_world.py",
            )

    # Build data
    if add_data_dir:
        data_path = project_root / "data"
        data_path.mkdir()
        with open(data_path / ".gitignore", "w+") as f:
            f.write("#Ignore all data files\n.\n!.gitignore\n")

    # Build ml-related parts
    if is_ml_project:
        model_savepath = project_root / "models"
        model_savepath.mkdir()
        with open(model_savepath / ".gitignore", "w+") as f:
            f.write("#Ignore all models checkpoints\n.\n!.gitignore\n")

        ml_path = src_path / "ml"
        ml_path.mkdir()

        models_path = ml_path / "models"
        models_path.mkdir()
        (models_path / "__init__.py").touch()
        with open(models_path / "abstract_model.py", "w+") as f:
            f.write(
                (PackagePaths.TEMPLATES / "ml_dir_files" / "abstract_model.py")
                .read_text()
                .replace("PACKAGE_NAME", package_name)
            )

        trainer_path = ml_path / "trainers"
        trainer_path.mkdir()
        (trainer_path / "__init__.py").touch()
        with open(trainer_path / "abstract_trainer.py", "w+") as f:
            f.write(
                (PackagePaths.TEMPLATES / "ml_dir_files" / "abstract_trainer.py")
                .read_text()
                .replace("PACKAGE_NAME", package_name)
            )

    # Build fastapi backend-related parts
    if fastapi_backend:
        backend_path = project_root / "backend"
        backend_path.mkdir()

        shutil.copy(
            PackagePaths.TEMPLATES / "backend_dir_files" / ".env",
            backend_path / ".env",
        )

        fastapi_test_path = backend_path / "tests"
        fastapi_test_path.mkdir()
        (fastapi_test_path / "__init__.py").touch()
        shutil.copy(
            PackagePaths.TEMPLATES / "backend_dir_files" / "conftest.py",
            backend_path / "tests" / "conftest.py",
        )
        shutil.copy(
            PackagePaths.TEMPLATES / "backend_dir_files" / "test_hello.py",
            backend_path / "tests" / "test_hello.py",
        )

        fastapi_app_path = backend_path / "app"
        fastapi_app_path.mkdir()
        (fastapi_app_path / "__init__.py").touch()
        shutil.copy(
            PackagePaths.TEMPLATES / "backend_dir_files" / "main.py",
            backend_path / "app" / "main.py",
        )
        shutil.copy(
            PackagePaths.TEMPLATES / "backend_dir_files" / "schemas.py",
            backend_path / "app" / "schemas.py",
        )
        shutil.copy(
            PackagePaths.TEMPLATES / "backend_dir_files" / "config.py",
            backend_path / "app" / "config.py",
        )
        shutil.copy(
            PackagePaths.TEMPLATES / "backend_dir_files" / "application_factory.py",
            backend_path / "app" / "application_factory.py",
        )

        fastapi_routers_path = fastapi_app_path / "routers"
        fastapi_routers_path.mkdir()
        (fastapi_routers_path / "__init__.py").touch()
        shutil.copy(
            PackagePaths.TEMPLATES / "backend_dir_files" / "hello.py",
            backend_path / "app" / "routers" / "hello.py",
        )

    # Build tests folder
    if not no_test_folder:
        test_path = project_root / "tests"
        test_path.mkdir()
        (test_path / ".gitkeep").touch()

    if run_install:
        os.system(f"cd {project_name} && bash .install.sh")
