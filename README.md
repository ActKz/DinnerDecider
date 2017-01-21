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

### Modify settings to fit your domain/ip
- DinnderDecider/settings.py
- DinnderDecider/views.py

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

## API Fields Define
Fields may appear in required fields or response data.

### User

Field name | Description
--- | ---
username | Account name
password | Account password
email | Account email
last_login | User last login time
date_joined | Acount created date

### UserFavList

Field name | Description
--- | ---
listName_id | List's unique id
listName | List's name

### UserFavListElement
Field name | Description
--- | ---
listElement_id | List element's unique id, **appear in storesData**
username | Account name
listName_id | List's unique id
listName | List's name
*storesData* | Contain all the store's fields

### Store
Field name | Description
--- | ---
store_id | Store unique id
store_name | Store's name
store_address | Store's address
store_phone | Store's phone
store_type | Store type's name
store_typeId | Store type's unique id
store_area | Store area's name
store_areaId | Store area's unique id
store_avgPrice | Store's average price
store_imgURL | Store's image url
info_provider | Account name who gives these informations
keyword | Keyword used to search for stores

### Store Type
Field name | Description
--- | ---
store_type | Store type's name
store_typeId | Store type's unique id

### Store Area
Field name | Description
--- | ---
store_area | Store area's name
store_areaId | Store area's unique id
