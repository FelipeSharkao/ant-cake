#!/bin/bash

path=$(yarn global bin)
pwd=$(pwd)

ls "$path" -l | grep nodemon > /dev/null
[ $? -eq 1 ] && yarn global add nodemon


cd "$(dirname "$0")/src"

mypy="pipenv run mypy --strict app.py"
dev="pipenv run uvicorn app:app"

$path/nodemon -x "$mypy && $dev" -e py

cd "$pwd"