#!/bin/bash

PROGDIR=$(dirname "$0")
cd "${PROGDIR}" || exit
source ./venv/bin/activate
python3 main.py
deactivate