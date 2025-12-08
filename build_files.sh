#!/usr/bin/env bash

echo "Buildando o projeto..."

pip install -r requirements.txt
python3 manage.py migrate

python3 manage.py collectstatic --noinput --clear

echo "Build concluído!"