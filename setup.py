#!/usr/bin/env python

"""
====================
grep-pre-commit-hook
====================

Wrapper over grep for pre-commit_
Helps seeking for anti-patterns

.. _pre-commit: https://pre-commit.com
"""

from distutils.core import setup

setup(
    name="grep-pre-commit-hook",
    version="0.1.0",
    description="grep wrapper for pre-commit",
    author="Backmarket",
    author_email="TODO",
    url="https://github.com/BackMarket/grep-pre-commit-hook",
    packages=["grep_hook"],
    entry_points={"console_scripts": ["gphook=grep_hook.wrapper:main"]},
)
