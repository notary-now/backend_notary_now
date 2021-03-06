from django.shortcuts import render
from django.http import JsonResponse
from .models import User, Notary, Appointment
from .helpers.format_notary import format_notary
from .helpers.format_appointment import format_appointment
import requests
import json
from django.views.decorators.csrf import csrf_exempt
from .utils import AppointmentStatuses
from django.contrib.auth import authenticate

def notary_users_list(request):
    notaries = Notary.objects.filter(active='True').order_by('id')
    notary_data = []

    for notary in notaries:
        notary_data.append(format_notary(notary))

    return JsonResponse(notary_data, safe=False)

@csrf_exempt
def notary_detail(request, pk):
    notary = Notary.objects.filter(user_id=pk)
    user = User.objects.filter(id=pk)
    if notary:
        if request.method == 'GET':
            return JsonResponse(format_notary(notary[0]))
        elif request.method == 'PUT':
            notary_info = json.loads(request.body)
            try:
                notary.update(**notary_info['notary_values'])
                user.update(**notary_info['user_values'])
                return JsonResponse(format_notary(notary[0]))
            except:
                return JsonResponse({"error": "Unknown Fields Provided"}, status=400)
    else:
        return JsonResponse({'error': 'Notary Not Found'}, status=404)

def notary_verify(request, pk):
    notary = Notary.objects.filter(user_id=pk)
    if notary:
        notary_id = notary[0].state_notary_number
        commission_date = notary[0].commission_date
        expiration_date = notary[0].expiration_date

        response = requests.get(f'https://data.colorado.gov/resource/k4uv-yvnk.json?notaryid={notary_id}&commissionstart={commission_date}&commissionexpire={expiration_date}').json()
        if response:
            notary.update(verified='True')
            return JsonResponse({'success': 'Verified'}, status=200)
        else:
            return JsonResponse({'error': 'Unable to verify'}, status=404)
    else:
        return JsonResponse({'error': 'Notary not Found'}, status=404)

@csrf_exempt
def appointments(request, pk):
    notary = Notary.objects.filter(user_id=pk)
    if notary:
        if request.method == 'GET':
            appointments = Appointment.objects.filter(notary_id=pk).order_by('status', 'date', 'time')
            appointment_data = []
            for appointment in appointments:
                appointment_data.append(format_appointment(appointment))

            return JsonResponse(appointment_data, safe=False)
        elif request.method == 'POST':
            appointment_info = json.loads(request.body)
            appointment = Appointment.objects.filter(
                notary_id=pk,
                appointee_id=appointment_info['appointee_id'],
                time=appointment_info['time'],
                date=appointment_info['date'],
                location=appointment_info['location'],
            )
            if not appointment:
                Appointment.objects.create(
                    notary_id=pk,
                    appointee_id=appointment_info['appointee_id'],
                    time=appointment_info['time'],
                    date=appointment_info['date'],
                    location=appointment_info['location'],
                )
                return JsonResponse({'success': 'Appointment Created'}, status=201)
            else:
                return JsonResponse({'error': 'Not Unique'}, status=400)
    else:
        return JsonResponse({'error': 'Notary Not Found'}, status=404)

@csrf_exempt
def appointment_detail(request, notary_user_id, appointment_id):
    appointment = Appointment.objects.filter(notary_id=notary_user_id, id=appointment_id)
    if appointment:
        if request.method == 'GET':
            return JsonResponse(format_appointment(appointment[0]), status=200, safe=False)
        elif request.method == 'PATCH':
            appointment_info = json.loads(request.body)
            if appointment_info['status']:
                try:
                    updated_appointment = appointment.update(status=getattr(AppointmentStatuses, appointment_info['status'].upper()).value)
                    return JsonResponse(format_appointment(appointment[0]), status=200, safe=False)
                except:
                    return JsonResponse({'error': 'Status Does Not Match'}, status=400, safe=False)
            else:
                return JsonResponse({'error': 'No Status Provided'}, status=400)
    else:
        return JsonResponse({'error': 'Notary Appointment Relation Not Found'}, status=400)

@csrf_exempt
def notary_users_login(request):
    notary_info = json.loads(request.body)
    user = authenticate(email=notary_info['email'], password=notary_info['password'])
    if user:
        notary = Notary.objects.filter(user_id=user.id)
        if notary:
            return JsonResponse(format_notary(notary[0]))
        else:
            return JsonResponse({'error': 'Notary Not Found'}, status=404)
    else:
        return JsonResponse({'error': 'User Not Found'}, status=404)

@csrf_exempt
def users_login(request):
    user_info = json.loads(request.body)
    user = authenticate(email=user_info['email'], password=user_info['password'])
    if user:
        return JsonResponse({
            "id": user.id,
            "email": user.email,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "zip_code": user.zip_code,
            "profile_photo": user.profile_photo,
        }, status=200)
    else:
        return JsonResponse({'error': 'User Not Found'}, status=404)
