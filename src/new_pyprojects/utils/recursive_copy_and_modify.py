import pathlib
from typing import Dict

from new_pyprojects.utils.check_flag import (
    check_flag,
    detect_flags_in_string,
    remove_flags_from_string,
)


def update_dst_name(
    dst: pathlib.Path,
    names_to_change: Dict[str, str],
):
    """Updates the destination name"""
    name = dst.name
    for key, value in names_to_change.items():

        name = name.replace(key, value)

    new_dst = dst.parent / name
    return new_dst


def process_and_copy_file(
    src: pathlib.Path,
    dst: pathlib.Path,
    names_to_change: Dict[str, str],
    flags: Dict[str, bool],
):
    dst = update_dst_name(dst, names_to_change)
    """Processes a file, and copies it to the destination"""
    with open(src, "r") as file:
        file_lines = file.readlines()
        lines_to_write = []

        for line in file_lines:
            # Check if line finished with "F:SOMETHING"
            if flag := detect_flags_in_string(line):
                if not check_flag(flag, flags):
                    continue
                else:
                    line = remove_flags_from_string(
                        line,
                        rstrip_chars=" \n"
                        + {
                            ".py": "#",
                            ".txt": "#",
                            ".sh": "#",
                            ".yaml": "#",
                            ".yml": "#",
                        }.get(src.suffix, ""),
                    )
            for key, value in names_to_change.items():
                line = line.replace(key, value)
            lines_to_write.append(line)

        with open(dst, "w") as new_file:
            new_file.writelines(lines_to_write)


def recurse_copy_and_modify(
    src: pathlib.Path,
    dst: pathlib.Path,
    names_to_change: Dict[str, str],
    flags: Dict[str, bool],
):
    """Recursively copies a directory from src to dst, modifying the files as it goes"""
    dst = update_dst_name(dst, names_to_change)
    dst.mkdir(exist_ok=True)

    for item in src.iterdir():
        if item.is_dir():

            copied_dir_name = item.name

            # If dir name looks like "F:CLI", and the flag is not set, skip it
            # if not skipped, the content of the directory should directly be copied
            # to the destination directory without creating a new directory

            if flag := detect_flags_in_string(copied_dir_name):
                if check_flag(flag, flags):
                    for subitem in item.iterdir():
                        if subitem.is_dir():
                            new_dir = dst / subitem.name
                            recurse_copy_and_modify(
                                subitem, new_dir, names_to_change, flags
                            )
                        else:
                            new_file = dst / subitem.name
                            process_and_copy_file(
                                subitem, new_file, names_to_change, flags
                            )
                else:
                    pass
            else:
                new_dir = dst / item.name
                recurse_copy_and_modify(item, new_dir, names_to_change, flags)

        else:
            process_and_copy_file(item, dst / item.name, names_to_change, flags)
