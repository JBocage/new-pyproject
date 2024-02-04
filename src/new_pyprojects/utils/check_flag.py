import re
from typing import Dict, Optional


def check_flag(
    flag: str,
    flags: Dict[str, bool],
) -> bool:
    """Checks if a flag is set

    input can be like:
        - "F:CLI"
        - "F:CLI|API"
        - "F:CLI&API"
    """
    # Remove potential parenthesis
    flag = flag.strip("()")
    if flag.startswith("F:"):
        flag = flag[2:]

    if "|" in flag:
        split_flags = flag.split("|")
        return any([flags.get(f, False) for f in split_flags])
    elif "&" in flag:
        split_flags = flag.split("&")
        return all([flags.get(f, False) for f in split_flags])
    else:
        return flags.get(flag, False)


def detect_flags_in_string(
    string: str,
) -> str:
    """Detects flags in a string"""
    if match := re.search(r"\({0,1}F:[\w\&\|]+\){0,1}", string):
        return match.group()
    else:
        return ""


def remove_flags_from_string(
    string: str,
    rstrip_chars: Optional[str] = None,
) -> str:
    """Removes flags from a string"""
    cleaned_string = string.replace(detect_flags_in_string(string), "")

    if rstrip_chars:
        ended_with_linebreak = cleaned_string.endswith("\n")
        cleaned_string = cleaned_string.rstrip(rstrip_chars)
        if ended_with_linebreak:
            cleaned_string += "\n"

    return cleaned_string
