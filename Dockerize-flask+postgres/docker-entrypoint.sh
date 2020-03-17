#!/bin/sh
set -e
export FLASK_APP='app/app.py'
flask db upgrade
python app/app.py
