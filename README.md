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

### Endpoints / How to Use

#### Notary Users

###### Get List Of All Notaries
`GET` to `/api/v1/notaries`

Example Response:
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
`GET` to `/api/v1/notaries/:id`

Example response:
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
    "commission_date": "2020-02-19",
    "expiration_date": "2022-02-19",
    "verified": true,
    "active": true,
    "radius": 15,
    "bio": ""
  }
}
```

##### Appointments
###### Get List of All Appointments
`GET` to `/api/v1/notaries/:notary_user_id/appointments`

Successful response should look like:
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
    "status": "Pending",
    "time": "23:15:42",
    "date": "2020-02-28",
    "location": "Irving, TX, USA"
  }
]
```

###### Get An Appointment By Id
`GET` to `/api/v1/notaries/:notary_user_id/appointments/:appointment_id`

Successful response should look like:
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
`POST` to `/api/v1/notaries/:notary_user_id/appointments`

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
`GET` to `/api/v1/notaries/:id/verify`

Successful response should look like:
```
{
    "success": "Verified"
}
```

Unsuccessful response should look like:
```
{
    "error": "Unable to verify"
}
```

##### Unsuccessful Responses
###### Appointments
```
Status: 400 / 500

{
    "error": "Notary Appointment Relation Not Found"
}
```
