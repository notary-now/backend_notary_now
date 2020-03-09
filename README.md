# NotaryNow
[![Build Status](https://travis-ci.org/notary-now/backend_notary_now.svg?branch=master)](https://travis-ci.org/notary-now/backend_notary_now)

![NotaryNow Screenshot](https://user-images.githubusercontent.com/38663414/76260135-160b5000-624f-11ea-8daa-03e4528e3325.png)

## Backend Service

### Jump To
- [About](#about)
- [Setup](#setup)
- [Required Python Packages](#required-python-packages)
- [Setup Database](#setup-database)
- [Environment Variables](#environment-variables)
- [Testing](#testing)
- [Running Tests](#running-tests)
- [Endpoints](#endpoints)
- [Database Schema](#database-schema)


### About

NotaryNow connects notaries with people who need notary service.

### Setup

1. Clone down repo using `git clone git@github.com:notary-now/backend_notary_now.git`
1. Change into project directory
1. Install Required Python Packages
1. Setup Database
1. Add Environment Variables

#### Required Python Packages
Install required Python Packages using the command: `pip install -r requirements.txt `

#### Setup Database
```
psql
CREATE DATABASE backend_notary_now_dev;
\q
```

#### Environment Variables
```
SECRET=<SECRET>
DBNAME=<DBNAME>
DBUSER=<DBUSER>
DBPASSWORD=<DBPASSWORD>
DBHOST=<DBHOST>
DBPORT=<DBPORT>
```

### Testing

Testing is done with `test`.

#### Running Tests

All tests can be run using the command `python manage.py test notary_now_api`

### Endpoints

#### Notary Users
###### Get List Of All Notaries
`GET` to `/api/v1/notaries/`

Example successful response:
```
Status: 200

[
  {
    "id": 1,
    "first_name": "Nancy",
    "last_name": "Notarelli",
    "email": "notary@notarynow.com",
    "profile_photo": "https://ca.slack-edge.com/T029P2S9M-UKFR53NRH-ce9206fa99d8-512",
    "zip_code": 80222,
    "notary_values": {
      "state_notary_number": "9128375620",
      "commission_date": "2020-02-19",
      "expiration_date": "2022-02-19",
      "verified": true,
      "active": true,
      "radius": 15,
      "bio": ""
    }
  },
  {
    "id": 2,
    "first_name": "Chester",
    "last_name": "Doodle",
    "email": "chester@chester.com",
    "profile_photo": "https://ca.slack-edge.com/T029P2S9M-UKFA99FBQ-de342b31c1f0-512",
    "zip_code": 90210,
    "notary_values": {
      "state_notary_number": "9128375633",
      "commission_date": "2020-02-19",
      "expiration_date": "2022-02-19",
      "verified": false,
      "active": true,
      "radius": 10,
      "bio": "My name is David and I have been a notary for one year now. I love helping people and using my notary skills. I hope to work with you soon!"
    }
  }
]
```

##### Notary Profile
###### Get Notary Profile by Id
`GET` to `/api/v1/notaries/:id/`

Example successful response:
```
Status: 200

{
  "id": 1,
  "first_name": "Tommy",
  "last_name": "Tank",
  "email": "notary@notarynow.com",
  "profile_photo": "https://ca.slack-edge.com/T029P2S9M-UKFR53NRH-ce9206fa99d8-512",
  "zip_code": 80222,
  "notary_values": {
    "state_notary_number": "9128375633",
    "commission_date": "2020-02-19",
    "expiration_date": "2022-02-19",
    "verified": true,
    "active": true,
    "radius": 15,
    "bio": ""
  }
}
```

###### Edit Notary Profile by Id
`PUT` to `/api/v1/notaries/:id/`

Example request payload:
```
{
  "id": 1,
  "user_values": {
    "first_name": "Mark",
    "last_name": "James",
    "email": "mark@james.com",
    "zip_code": 12345
  },
  "notary_values": {
    "state_notary_number": "9128375633",
    "radius": 7,
    "active": true,
    "bio": "New Bio!",
    "commission_date": "2020-03-23",
    "expiration_date": "2023-03-23"
  }
}
```

Example successful response:
```
Status: 200

{
  "id": 1,
  "first_name": "Mark",
  "last_name": "James",
  "email": "mark@james.com",
  "profile_photo": "https://ca.slack-edge.com/T029P2S9M-UKFR53NRH-ce9206fa99d8-512",
  "zip_code": 12345,
  "notary_values": {
    "commission_date": "2020-03-23",
    "expiration_date": "2023-03-23",
    "verified": true,
    "active": true,
    "radius": 7,
    "bio": "New Bio!"
  }
}
```

##### Appointments
###### Get List of All Appointments
`GET` to `/api/v1/notaries/:notary_user_id/appointments/`

Example successful response:
```
Status: 200

[
  {
    "id": 1,
    "notary": {
      "name": "William Warrick",
      "id": 2
    },
    "appointee": {
      "name": "Nancy Noteralli",
      "id": 1
    },
    "status": "Pending",
    "time": "23:15:42",
    "date": "2020-02-20",
    "location": "Irving, TX, USA"
  },
  {
    "id": 2,
    "notary": {
      "name": "William Warrick",
      "id": 2
    },
    "appointee": {
      "name": "Nancy Noteralli",
      "id": 1
    },
    "status": "Completed",
    "time": "23:15:42",
    "date": "2020-02-28",
    "location": "Irving, TX, USA"
  }
]
```

###### Get An Appointment By Id
`GET` to `/api/v1/notaries/:notary_user_id/appointments/:appointment_id`

Example successful response:
```
Status: 200

{
   "id": 1,
   "notary": {
     "name": "William Warrick",
     "id": 2
   },
   "appointee": {
     "name": "Nancy Noteralli",
     "id": 1
   },
   "status": "Pending",
   "time": "23:15:42",
   "date": "2020-02-20",
   "location": "Irving, TX, USA"
 }
```

###### Make an Appointment
`POST` to `/api/v1/notaries/:notary_user_id/appointments/`

Request payload should look like:
```
{
    "appointee_id": 2,
    "time": "14:00:00",
    "date": "2020-09-12",
    "location": "123 Main St."
}
```

###### Update an Appointment Status
`PATCH` to `/api/v1/notaries/:notary_user_id/appointments/:appointment_id`

Request payload should look like:
```
{
    "status": "COMPLETED"
}
```

##### Notary Profile Verifications
`GET` to `/api/v1/notaries/:id/verify/`

Example successful response:
```
Status: 200

{
    "success": "Verified"
}
```

##### Unsuccessful Responses
All endpoints are equipped to handle client errors and will return the one of the following status codes with error messages:

|Status Code|Reason|
|:-:|---|
| 400  | Bad request sent  |
| 404  | Resource not found in the database  |

##### Database Schema
![NotaryNow DB Schema](https://user-images.githubusercontent.com/38663414/75284889-85278400-580d-11ea-8d5d-add01365f9ff.png)
