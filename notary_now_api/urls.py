from django.urls import path
from .views import notary_users_list, notary_detail, notary_verify, appointments

urlpatterns = [
    path("notaries/", notary_users_list, name="notary_users_list"),
    path("notaries/<int:pk>/", notary_detail, name="notary_user_detail"),
    path("notaries/<int:pk>/appointments", appointments, name="notary_appointments"),
    path("notaries/<int:pk>/verify/", notary_verify, name="notary_user_verify")
]
