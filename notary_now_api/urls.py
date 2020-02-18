from django.urls import path
from .views import notary_users_list, notary_detail

urlpatterns = [
    path("notaries/", notary_users_list, name="notary_users_list"),
    path("notaries/<int:pk>/", notary_detail, name="notary_user_detail")
]
