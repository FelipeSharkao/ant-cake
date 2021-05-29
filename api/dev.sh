#!/bin/bash

path=$(yarn global bin)

ls "$path" -l | grep nodemon > /dev/null
[ $? -eq 1 ] && yarn global add nodemon

prepend() {
  echo "while read line; do echo \"[$1] \$line\"; done"
}

coco="pipenv run coconut src generated --target 3.8 -lk --mypy --strict"
coco+=" | $(prepend coco)"
app="FLASK_ENV=development pipenv run flask run --no-reload | $(prepend app)"

$path/nodemon -x "$coco && $app" -e py,coco,json,yaml --ignore generated