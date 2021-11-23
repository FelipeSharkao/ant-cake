#!/bin/bash

path=$(yarn global bin)
pwd=$(pwd)

ls "$path" -l | grep nodemon > /dev/null
[ $? -eq 1 ] && yarn global add nodemon

ls "$path" -l | grep pyright > /dev/null
[ $? -eq 1 ] && yarn global add pyright

cd "$(dirname "$0")/src"
$path/nodemon -x "pyright && pipenv run uvicorn app:app" -e py
cd "$pwd"