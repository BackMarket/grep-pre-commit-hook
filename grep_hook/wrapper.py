"""
====================
grep-pre-commit-hook
====================

Wrapper over grep for pre-commit_
Helps seeking for anti-patterns

.. _pre-commit: https://pre-commit.com
"""

from argparse import ArgumentParser
from subprocess import call
from sys import exit as sysexit


def main():
    """
    Simple wrapper to avoid having to conform to UPPER_CASE naming style.

    It will be called by the `gphook` entry point.
    """

    parser = ArgumentParser(description="grep tool wrapper for pre-commit")

    parser.add_argument(
        "pattern",
        type=str,
        nargs=1,
        help="The pattern(s) passed to grep. "
        "You can pass multiple patterns as such: `(pattern1|...|patternN)`"
    )
    parser.add_argument("files", type=str, nargs="+", help="Files to grep")
    args = parser.parse_args()

    files = args.files
    pattern = args.pattern

    ret_val = call(["grep", "-nHo", "-E", pattern[0]] + files)
    sysexit(0 if ret_val == 1 else 1)


if __name__ == "__main__":
    main()
