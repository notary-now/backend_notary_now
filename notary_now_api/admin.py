from django.contrib import admin

# Register your models here.
from .models import Location, Language, Notary, Appointment
admin.site.register(Location)
admin.site.register(Language)
admin.site.register(Notary)
admin.site.register(Appointment)
