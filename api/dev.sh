#!/bin/bash

ls $(yarn global bin) -l | grep concurrently > /dev/null
[ $? -eq 1 ] && yarn global add concurrently

coco="pipenv run coconut src generated --target 3.8 -lkw --mypy --strict"
app="pipenv run python app.py"

$(yarn global bin)/concurrently -skn coconut,app "$coco" "$app"