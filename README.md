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
- API
  - User
    - create account
    - change password
    - change email
    - user info
  - Store
    - add  store
    - update store
    - list store: fuzzy search for several fields
    - get store
    - delete store
  - Store Type
    - add type
    - list type
    - delete type
  - Store Area
    - add area
    - list area
    - delete area
  - User favorite list
    - add list
    - list list
    - update list
    - delete list
  - User favorite list element
    - add element
    - list element
    - delete element


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

## Run test

### No testing details

```
cd DinnerDecider
python manage.py test
```

### Show coverage and testing details

This will run `python manage.py test` , use [coverage](https://coverage.readthedocs.io/en/coverage-4.3.1/) to detect the testing coverage and generate report to http://0.0.0.0:8000
```
./gen_coverage_report
```
