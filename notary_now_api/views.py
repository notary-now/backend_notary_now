from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, HttpResponse
from .models import User, Notary

def notary_users_list(request):
    notaries = Notary.objects.select_related('user')

    notary_data = []

    for notary in notaries:
        notary_data.append({
            "id": notary.user.id,
            "first_name": notary.user.first_name,
            "last_name": notary.user.last_name,
            "email": notary.user.email,
            "profile_photo": notary.user.profile_photo,
            "zip_code": notary.user.zip_code,
            "notary_values": {
                "commission_date": notary.commission_date,
                "expiration_date": notary.expiration_date,
                "verified": notary.verified,
                "active": notary.active,
                "radius": notary.radius,
                "bio": notary.bio
            }
        })

    return JsonResponse(notary_data, safe=False)

def notary_detail(request, pk):
    notary = Notary.objects.filter(user_id=pk)
    if notary:
        notary = notary.select_related('user')[0]
        data = {
            "id": notary.user.id,
            "first_name": notary.user.first_name,
            "last_name": notary.user.last_name,
            "email": notary.user.email,
            "profile_photo": notary.user.profile_photo,
            "zip_code": notary.user.zip_code,
            "notary_values": {
                "commission_date": notary.commission_date,
                "expiration_date": notary.expiration_date,
                "verified": notary.verified,
                "active": notary.active,
                "radius": notary.radius,
                "bio": notary.bio
            }
        }
        return JsonResponse(data)
    else:
        return JsonResponse({'error': 'Notary not Found'}, status=404)
