from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, HttpResponse
from .models import User, Notary, Appointment
from .helpers.format_notary import format_notary
import requests
import json
from django.views.decorators.csrf import csrf_exempt

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

def notary_verify(request, pk):
    notary = Notary.objects.filter(user_id=pk)[0]
    if notary:
        notary_id = notary.state_notary_number
        commission_date = notary.commission_date
        expiration_date = notary.expiration_date

        response = requests.get(f'https://data.colorado.gov/resource/k4uv-yvnk.json?notaryid={notary_id}&commissionstart={commission_date}&commissionexpire={expiration_date}').json()
        if response:
            notary.update(verified='True')
            return JsonResponse({'success': 'Verified'}, status=200)
        else:
            return JsonResponse({'error': 'Unable to verify'}, status=404)
    else:
        return JsonResponse({'error': 'Notary not Found'}, status=404)

@csrf_exempt
def make_appointment(request, pk):
    notary = Notary.objects.filter(user_id=pk)[0]
    if notary:
        appointment_info = json.loads(request.body)
        appointment = Appointment.objects.filter(
            notary_id=pk,
            apointee_id=appointment_info['apointee_id'],
            time=appointment_info['time'],
            date=appointment_info['date'],
            location=appointment_info['location'],
        )
        if not appointment:
            Appointment.objects.create(
                notary_id=pk,
                apointee_id=appointment_info['apointee_id'],
                time=appointment_info['time'],
                date=appointment_info['date'],
                location=appointment_info['location'],
            )
            return JsonResponse({'success': 'Appointment Created'}, status=201)
        else:
            return JsonResponse({'error': 'Not Unique'}, status=400)
    else:
        return JsonResponse({'error': 'Notary not Found'}, status=404)
