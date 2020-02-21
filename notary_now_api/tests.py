from .models import User, Notary, Appointment
from django.test import RequestFactory, TestCase
from django.contrib.auth import get_user_model
User = get_user_model()
import json

from .views import notary_users_list, notary_detail, appointments

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
        request = self.factory.get('/api/v1/notaries/1')
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
