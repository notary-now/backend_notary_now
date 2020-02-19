from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import User, Notary

def notary_users_list(request):
    users = User.objects.filter(is_notary='True')

    data = {"results": list(users.values("id", "first_name", "last_name", "profile_photo", "zip_code"))}
    
    return JsonResponse(data)

def notary_detail(request, pk):
    user = get_object_or_404(User, pk=pk)

    notary_information = Notary.objects.filter(user_id=user.id)

    data = {"results": {
        "id": user.id,
        "first_name": user.first_name,
        "last_name": user.last_name,
        "email": user.email,
        "profile_photo": user.profile_photo,
        "zip_code": user.zip_code,
        "notary_values": list(notary_information.values("commission_date", "expiration_date", "verified", "active", "radius"))
    }}
    return JsonResponse(data)
