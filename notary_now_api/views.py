from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import User, Notary

def notary_users_list(request):
    users = User.objects.select_related('notary')

    data = {"results": list(users.values("id", "first_name", "last_name", "profile_photo"))}
    return JsonResponse(data)

def notary_detail(request, pk):
    user = get_object_or_404(User, pk=pk)
    languages = Language.objects.filter(user_id=user.id)
    data = {"results": {
        "first_name": user.first_name,
        "last_name": user.last_name,
        "languages": list(languages.values("primary_language", "secondary_language", "tertiary_language"))
    }}
    return JsonResponse(data)
