#/bin/sh
path=${PWD##*/}
project="DinnerDecider"
covdir="htmlcov"

cd ${project}
coverage run --source='.' manage.py test
coverage report
coverage html
cd ${covdir}
python -m http.server
