from django.urls import path
from .views import notary_users_list, notary_detail, notary_verify, appointments, appointment_detail, notary_users_login, users_login

urlpatterns = [
    path("notaries/", notary_users_list, name="notary_users_list"),
    path("notaries/login/", notary_users_login, name="notary_users_login"),
    path("users/login/", users_login, name="users_login"),
    path("notaries/<int:pk>/", notary_detail, name="notary_user_detail"),
    path("notaries/<int:notary_user_id>/appointments/<int:appointment_id>/", appointment_detail, name="notary_appointment_detail"),
    path("notaries/<int:pk>/appointments/", appointments, name="notary_appointments"),
    path("notaries/<int:pk>/verify/", notary_verify, name="notary_user_verify")
]
