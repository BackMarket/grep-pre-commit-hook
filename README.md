# grep-pre-commit-hook

Grep hook for [pre-commit](http://pre-commit.com/) to search for anti-patterns

## Why ?

There are patterns we don't want to see in our code and grep is useful tool for
seeking patterns in files. The problem there is that grep does not natively run
well with pre-commit since it returns 0 (a success) when it founds a pattern.

We are searching for anti-patterns, hence a success would be grep not finding
those. This pre-commit hook wraps grep for it to work the way we want.

