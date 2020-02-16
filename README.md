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

##### Notary Profile
###### Get Notary Profile by Id
`GET` to `/notaries/:id`
###### Edit Notary Profile by Id
`PUT` to `/notaries/:id`

##### Find A Notary
###### Get List Of All Notaries
`GET` to `/notaries`

##### Appointments
###### Get List of All Appointments
`GET` to `/notaries/:user_id/appointments`
###### Get Appointment by Id
`GET` to `/notaries/:user_id/appointments/:id`
###### Make an Appointment
`POST` to `/notaries/:user_id/appointments`
###### Delete Appointment by Id
`DELETE to `/notaries/:user_id/appointments/:id`

##### Languages
###### Get List of Languages
`GET` to `/notaries/:user_id/languages`
###### Edit Languages
`PUT` to `/notaries/:user_id/languages/:id`
###### Remove a Language
`DELETE to `/notaries/:user_id/languages/:id`

##### Locations
###### Get List of Locations
`GET` to `/notaries/:user_id/locations`
###### Add a Location
`POST` to `/notaries/:user_id/locations`
###### Edit a Location
`PUT` to `/notaries/:user_id/locations/:id``
###### Remove a Location
`DELETE to `/notaries/:user_id/languages/:id`