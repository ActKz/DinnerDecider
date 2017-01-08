# DinnerDecider

## Dependency

- [django-cors-headers](https://github.com/ottoyiu/django-cors-headers)
- [Django](https://www.djangoproject.com/)
- [djangorestframework](https://github.com/tomchristie/django-rest-framework)
- [djangorestframework-jwt](https://github.com/GetBlimp/django-rest-framework-jwt)
- [django-rest-swagger](https://github.com/marcgibbons/django-rest-swagger)
- [coverage](https://coverage.readthedocs.io/en/coverage-4.3.1/)
- [django-sslserver](https://github.com/teddziuba/django-sslserver)

## Feature

- Browsable API by using django-rest-swagger
- Self defined models CRUD
  - Account C/R/U
  - Store C/R/U/D
  - Store Type C/R/D
  - Area C/R/D
  - User favorite list C/R/U/D
  - User favorite listname C/R/U/D

## Usage

### Install the dependency
```
pip install -r requirements.txt
```

### Make migrations
```
cd DinnerDecider
python manage.py makemigrations
python mange.py migrate
```

### Run server
```
python manage.py runsslserver
```
