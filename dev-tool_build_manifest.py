"""
Run this file to regenerate the MANIFEST.in
"""

from pathlib import Path
from typing import List

from new_pyprojects.utils.paths import Paths


# Function that recursively returns the paths of all subdirectories in a directory
def get_subdirectories(directory: Path) -> List[Path]:
    paths = []

    for path in directory.iterdir():
        if path.is_dir():
            paths.append(path)
            paths += get_subdirectories(path)

    return paths


with open(Paths.ROOT / "MANIFEST.in", "w+") as f:
    for path in get_subdirectories(Paths.TEMPLATE):
        f.write(f"recursive-include {path.relative_to(Paths.ROOT)} *\n")
