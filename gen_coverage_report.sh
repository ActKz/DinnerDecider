#/bin/sh
path=${PWD##*/}
project="DinnerDecider"
covdir="htmlcov"
include="store/views.py,account/views.py"

if [ -d ${project} ]; then
    cd ${project}
    echo -e "Changing directory to <$project>"
else
    echo -e "ERROR: Cannot change directory to <$project>"
    exit 1
fi
if [ -d ${covdir} ]; then
    rm -r ${covdir}
    echo -e "Deleting old html file"
fi
if [ -f "manage.py" ]; then
    coverage run --source='.' manage.py test
    coverage report --include="$include"
    coverage html --include="$include"
else
    echo -e "ERROR: manage.py not exist"
    exit 1
fi
if [ -d ${covdir} ]; then
    cd ${covdir}
    echo -e "Changing directory to <$covdir>"
else
    echo -e "ERROR: Cannot change directory to <$covdir>"
    exit 1
fi
python -m http.server
