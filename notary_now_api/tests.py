from .models import User, Notary, Appointment
from django.test import RequestFactory, TestCase
from django.contrib.auth import get_user_model
User = get_user_model()
import json

from .views import notary_users_list, notary_detail, appointments, appointment_detail

class AllNotaryTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            first_name='David', last_name='Smith', email='jacob@turing.edu')
        self.notary = Notary.objects.create(
            state_notary_number='12345678',
            commission_date='2020-02-10',
            expiration_date='2022-02-10',
            radius=7,
            user_id=self.user.id
        )

    def test_notaries_endpoint(self):
        request = self.factory.get('/api/v1/notaries')
        response = notary_users_list(request)

        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.content)
        self.assertEqual(json_response[0]['first_name'], self.user.first_name)
        self.assertEqual(json_response[0]['last_name'], self.user.last_name)
        self.assertEqual(json_response[0]['email'], self.user.email)
        self.assertEqual(json_response[0]['notary_values']['commission_date'], self.notary.commission_date)
        self.assertEqual(json_response[0]['notary_values']['expiration_date'], self.notary.expiration_date)
        self.assertEqual(json_response[0]['notary_values']['active'], self.notary.active)
        self.assertEqual(json_response[0]['notary_values']['verified'], self.notary.verified)
        self.assertEqual(json_response[0]['notary_values']['bio'], self.notary.bio)

class OneNotaryTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            first_name='David', last_name='Smith', email='jacob@turing.edu')
        self.notary = Notary.objects.create(
            state_notary_number='12345678',
            commission_date='2020-02-10',
            expiration_date='2022-02-10',
            radius=7,
            user_id=self.user.id
        )

    def test_notaries_endpoint(self):
        request = self.factory.get(f'/api/v1/notaries/{self.user.id}')
        response = notary_detail(request, self.user.id)

        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.content)
        self.assertEqual(json_response['first_name'], self.user.first_name)
        self.assertEqual(json_response['last_name'], self.user.last_name)
        self.assertEqual(json_response['email'], self.user.email)
        self.assertEqual(json_response['notary_values']['commission_date'], self.notary.commission_date)
        self.assertEqual(json_response['notary_values']['expiration_date'], self.notary.expiration_date)
        self.assertEqual(json_response['notary_values']['active'], self.notary.active)
        self.assertEqual(json_response['notary_values']['verified'], self.notary.verified)
        self.assertEqual(json_response['notary_values']['bio'], self.notary.bio)

class MakeAppointmentTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            first_name='David', last_name='Smith', email='jacob@turing.edu')
        self.appointee = User.objects.create_user(
            first_name='Karen', last_name='Smith', email='karen@turing.edu')
        self.notary = Notary.objects.create(
            state_notary_number='12345678',
            commission_date='2020-02-10',
            expiration_date='2022-02-10',
            radius=7,
            user_id=self.user.id
        )

    def test_appointments_endpoint(self):
        request = self.factory.post(f'/api/v1/notaries/{self.user.id}/appointments',
        data=json.dumps({
            "appointee_id": self.appointee.id,
            "date": "2020-02-28",
            "time": "23:15:42",
            "location": "Irving, TX, USA"
         }),
         content_type='application/json')
        response = appointments(request, self.user.id)

        self.assertEqual(response.status_code, 201)
        json_response = json.loads(response.content)
        self.assertEqual(json_response['success'], 'Appointment Created')

class AllAppointmentsTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            first_name='David', last_name='Smith', email='jacob@turing.edu')
        self.appointee = User.objects.create_user(
            first_name='Karen', last_name='Smith', email='karen@turing.edu')
        self.notary = Notary.objects.create(
            state_notary_number='12345678',
            commission_date='2020-02-10',
            expiration_date='2022-02-10',
            radius=7,
            user_id=self.user.id
        )
        self.appointment_one = Appointment.objects.create(
            notary_id=self.user.id,
            appointee_id=self.appointee.id,
            date='2020-04-28',
            time='23:15:42',
            location='Irving, TX, USA'
        )
        self.appointment_two = Appointment.objects.create(
            notary_id=self.user.id,
            appointee_id=self.appointee.id,
            date='2020-03-04',
            time='22:15:42',
            location='Irving, TX, USA'
        )
        self.appointment_three = Appointment.objects.create(
            notary_id=self.user.id,
            appointee_id=self.appointee.id,
            date='2020-02-27',
            time='23:15:42',
            location='Irving, TX, USA',
            status=2
        )
        self.appointment_four = Appointment.objects.create(
            notary_id=self.user.id,
            appointee_id=self.appointee.id,
            date='2020-04-04',
            time='23:15:42',
            location='Irving, TX, USA',
            status=3
        )

    def test_appointments_endpoint(self):
        request = self.factory.get(f'/api/v1/notaries/{self.user.id}/appointments')

        response = appointments(request, self.user.id)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.content)

        self.assertEqual(json_response[0]['notary']['id'], self.user.id)
        self.assertEqual(json_response[0]['notary']['name'], self.user.first_name + " " + self.user.last_name)
        self.assertEqual(json_response[0]['id'], self.appointment_two.id)
        self.assertEqual(json_response[0]['appointee']['id'], self.appointee.id)
        self.assertEqual(json_response[0]['appointee']['name'], self.appointee.first_name + " " + self.appointee.last_name)
        self.assertEqual(json_response[0]['location'], self.appointment_two.location)
        self.assertEqual(json_response[0]['date'], self.appointment_two.date)
        self.assertEqual(json_response[0]['time'], self.appointment_two.time)
        self.assertEqual(json_response[0]['status'], self.appointment_two.get_appointment_result)

        self.assertEqual(json_response[1]['date'], self.appointment_one.date)
        self.assertEqual(json_response[1]['time'], self.appointment_one.time)
        self.assertEqual(json_response[1]['id'], self.appointment_one.id)
        self.assertEqual(json_response[1]['notary']['id'], self.user.id)
        self.assertEqual(json_response[1]['appointee']['id'], self.appointee.id)
        self.assertEqual(json_response[1]['location'], self.appointment_one.location)
        self.assertEqual(json_response[2]['id'], self.appointment_three.id)
        self.assertEqual(json_response[3]['id'], self.appointment_four.id)


class GetAppointmentTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            first_name='David', last_name='Smith', email='jacob@turing.edu')
        self.appointee = User.objects.create_user(
            first_name='Karen', last_name='Smith', email='karen@turing.edu')
        self.notary = Notary.objects.create(
            state_notary_number='12345678',
            commission_date='2020-02-10',
            expiration_date='2022-02-10',
            radius=7,
            user_id=self.user.id
        )
        self.appointment_one = Appointment.objects.create(
            notary_id=self.user.id,
            appointee_id=self.appointee.id,
            date='2020-02-28',
            time='23:15:42',
            location='Irving, TX, USA'
        )
        self.appointment_two = Appointment.objects.create(
            notary_id=self.user.id,
            appointee_id=self.appointee.id,
            date='2020-03-04',
            time='23:16:42',
            location='Irving, TX, USA'
        )

    def test_appointment_endpoint(self):
        request = self.factory.get(f'/api/v1/notaries/{self.user.id}/appointments/{self.appointment_one.id}')

        response = appointment_detail(request, self.user.id, self.appointment_one.id)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.content)

        self.assertEqual(json_response['notary']['id'], self.user.id)
        self.assertEqual(json_response['notary']['name'], self.user.first_name + " " + self.user.last_name)
        self.assertEqual(json_response['id'], self.appointment_one.id)
        self.assertEqual(json_response['appointee']['id'], self.appointee.id)
        self.assertEqual(json_response['appointee']['name'], self.appointee.first_name + " " + self.appointee.last_name)
        self.assertEqual(json_response['location'], self.appointment_one.location)
        self.assertEqual(json_response['date'], self.appointment_one.date)
        self.assertEqual(json_response['time'], self.appointment_one.time)
        self.assertEqual(json_response['status'], self.appointment_one.get_appointment_result)

        self.assertNotEqual(json_response['id'], self.appointment_two.id)
        self.assertNotEqual(json_response['time'], self.appointment_two.time)

    def test_appointment_endpoint_sad_path(self):
        request = self.factory.get(f'/api/v1/notaries/20/appointments/{self.appointment_one.id}')
        response = appointment_detail(request, 20, self.appointment_one.id)
        self.assertEqual(response.status_code, 400)

class ChangeAppointmentStatusTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            first_name='David', last_name='Smith', email='jacob@turing.edu')
        self.appointee = User.objects.create_user(
            first_name='Karen', last_name='Smith', email='karen@turing.edu')
        self.notary = Notary.objects.create(
            state_notary_number='12345678',
            commission_date='2020-02-10',
            expiration_date='2022-02-10',
            radius=7,
            user_id=self.user.id
        )
        self.appointment_one = Appointment.objects.create(
            notary_id=self.user.id,
            appointee_id=self.appointee.id,
            date='2020-02-28',
            time='23:15:42',
            location='Irving, TX, USA'
        )

    def test_appointment_status_endpoint(self):
        request = self.factory.patch(f'/api/v1/notaries/{self.user.id}/appointments/{self.appointment_one.id}/',
        data=json.dumps({
            "status": "COMPLETED"
         }),
         content_type='application/json')

        response = appointment_detail(request, self.user.id, self.appointment_one.id)
        json_response = json.loads(response.content)
        self.assertEqual(response.status_code, 200)


        self.assertEqual(json_response['notary']['id'], self.user.id)
        self.assertEqual(json_response['notary']['name'], self.user.first_name + " " + self.user.last_name)
        self.assertEqual(json_response['id'], self.appointment_one.id)
        self.assertEqual(json_response['appointee']['id'], self.appointee.id)
        self.assertEqual(json_response['appointee']['name'], self.appointee.first_name + " " + self.appointee.last_name)
        self.assertEqual(json_response['location'], self.appointment_one.location)
        self.assertEqual(json_response['date'], self.appointment_one.date)
        self.assertEqual(json_response['time'], self.appointment_one.time)
        self.assertEqual(json_response['status'], 'Completed')

        request = self.factory.patch(f'/api/v1/notaries/{self.user.id}/appointments/{self.appointment_one.id}/',
        data=json.dumps({
            "status": "CANCELLED"
         }),
         content_type='application/json')

        response = appointment_detail(request, self.user.id, self.appointment_one.id)
        json_response = json.loads(response.content)

        self.assertEqual(json_response['status'], 'Cancelled')

    def test_appointment_status_endpoint_sadpath(self):
        request = self.factory.patch(f'/api/v1/notaries/{self.user.id}/appointments/{self.appointment_one.id}/',
        data=json.dumps({
            "status": ""
         }),
         content_type='application/json')

        response = appointment_detail(request, self.user.id, self.appointment_one.id)
        json_response = json.loads(response.content)
        self.assertEqual(response.status_code, 400)


        self.assertEqual(json_response['error'], 'No Status Provided')

        request = self.factory.patch(f'/api/v1/notaries/{self.user.id}/appointments/{self.appointment_one.id}/',
        data=json.dumps({
            "status": "asdfasdf"
         }),
         content_type='application/json')

        response = appointment_detail(request, self.user.id, self.appointment_one.id)
        json_response = json.loads(response.content)
        self.assertEqual(response.status_code, 400)


        self.assertEqual(json_response['error'], 'Status Does Not Match')
