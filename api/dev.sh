#!/bin/bash

path=$(yarn global bin)

ls "$path" -l | grep nodemon > /dev/null
[ $? -eq 1 ] && yarn global add nodemon

app="$(dirname "$0")/src/app.py"
mypy="pipenv run mypy --strict $app"
dev="FLASK_ENV=development FLASK_APP=$app pipenv run flask run"

$path/nodemon -x "$mypy && $dev" -e py -w src