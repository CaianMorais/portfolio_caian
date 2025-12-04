set -e

echo "Buildando o projeto..."

pip install -r requirements.txt

python3 manage.py migrate

npm install
npm run build:css

echo "Build concluído!"