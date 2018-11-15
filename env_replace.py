#!/usr/bin/env python3
"""
env-replace: un-expand environment variables for more compact output

Usage:

    some-big-output-producing-command | env-replace

"""

from collections import OrderedDict
import os
import sys

__version__ = '1.0.0'


def _sort_by_length(key_value):
    """Sort key, value pairs to prioritize shortest substitution

    - prioritize long strings first to ensure the longest match is substituted
    - prioritize short variable names in case two keys have the same value
    """
    key, value = key_value
    return (-len(value), len(key))


def main():
    # create ordered dict, sorted by length
    replacements = OrderedDict()
    assignments = {}
    for key, value in sorted(os.environ.items(), key=_sort_by_length):
        if len(value) > len(key) and value not in replacements:
            # only include substitutions that would shorten output
            # and only include the *shortest* environment variable
            # in case of multiple variables with the same value
            envvar = '$' + key
            replacements[value] = envvar
            assignments[envvar] = key + '='

    for line in sys.stdin:
        # perform replacements per line
        save_line = line
        for to_replace, envvar in replacements.items():
            if line.startswith(assignments[envvar]):
                # avoid rewriting assignments, e.g.
                # the output of `env` itself
                continue
            line = line.replace(to_replace, envvar)
        sys.stdout.write(line)


if __name__ == '__main__':
    main()
