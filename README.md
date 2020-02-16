# NotaryNow

## Backend Service

### About

NotaryNow connects notaries with people who need notary service.

### Setup

1. Clone down repo using `git clone git@github.com:notary-now/backend_notary_now.git`
1. Change into project directory
1. Install Required Python Packages
1. Setup Database
1. Add Environment Variables

#### Required Python Packages
- dotenv `pip3 install python-dotenv`
- psycop2 `pip3 install django psycop2`
- pytest `pip3 install -U pytest`
- whitenoise `pip3 install whitenoise`
- gunicorn `pip3 install gunicorn`
- django_heroku `pip3 install django-heroku`

### Setup Database
```
psql
CREATE DATABASE backend_notary_now_dev;
\q
```

### Environment Variables
```
SECRET=<SECRET>
DBNAME=<DBNAME>
DBUSER=<DBUSER>
DBPASSWORD=<DBPASSWORD>
DBHOST=<DBHOST>
DBPORT=<DBPORT>
```

### Testing

Testing is done with pytest.

#### Running Tests

All tests can be run using the command `pytest`

### Endpoints / How to Use

#### Notary Users