#!/bin/sh -e
set -x

autoflake --remove-all-unused-imports --recursive --remove-unused-variables --in-place src/app --exclude=__init__.py
black src/app
isort --recursive --apply src/app
