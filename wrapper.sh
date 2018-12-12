#!/bin/bash

BASENAME=$0

help_message() {
    echo "Error: script requires 0 or 1 variables"
    echo "Syntax: $1 [output_file]"
    echo
    return
}

if [ "$#" -gt 1 ]; then
    help_message "${BASENAME}"
    exit 1
fi

virtualenv env
source env/bin/activate
pip install -r requirements.txt
if [ -z $1 ]; then
    python google-drive-list-shared.py
else
    python google-drive-list-shared.py > $1
fi
