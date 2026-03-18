#!/bin/sh
set -e

python3 -m venv env

./env/bin/pip3 install --editable .["test"]

mkdir -p .pylint.d
export PYLINTHOME="$(pwd)/.pylint.d"

if ! ./env/bin/pytest; then
   echo -e "\e[31mpytest error!\e[0m"
   exit 1
fi

if ! ./env/bin/pylint $(git ls-files '*.py'); then
   echo "\e[31mpylint error!\e[0m"
   exit 1
fi

if ! ./env/bin/black --target-version py313 --check $(git ls-files '*.py'); then
   echo "\e[31mFormatting error!\e[0m"
   echo "Run ./env/bin/black --target-version py313 $(git ls-files '*.py') to fix"
   exit 1
fi

echo "\n\e[32mAll checks passed!\e[0m"
