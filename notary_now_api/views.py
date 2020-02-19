from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, HttpResponse
from .models import User, Notary
from .helpers.format_notary import format_notary

def notary_users_list(request):
    notaries = Notary.objects.select_related('user')

    notary_data = []

    for notary in notaries:
        notary_data.append(format_notary(notary))

    return JsonResponse(notary_data, safe=False)

def notary_detail(request, pk):
    notary = Notary.objects.filter(user_id=pk)
    if notary:
        notary = notary.select_related('user')[0]
        
        return JsonResponse(format_notary(notary))
    else:
        return JsonResponse({'error': 'Notary not Found'}, status=404)
