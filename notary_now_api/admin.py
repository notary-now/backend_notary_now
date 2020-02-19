from django.contrib import admin

# Register your models here.
from .models import Notary, Appointment, User
admin.site.register(Notary)
admin.site.register(Appointment)
admin.site.register(User)
