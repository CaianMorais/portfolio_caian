#!/usr/bin/env bash

echo "Buildando o projeto..."

pip install -r requirements.txt
python3 manage.py migrate

npm install
npm run build:css

python3 manage.py collectstatic --noinput

echo "Build concluído!"