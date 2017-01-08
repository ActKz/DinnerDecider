coverage run --source='.' manage.py test
coverage report
coverage html
cd htmlcov
python -m http.server
