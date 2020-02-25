from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from .models import Notary, Appointment, User
from django import forms

class MyUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = User


class MyUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User

class AccountAdmin(UserAdmin):
    form = MyUserChangeForm
    add_form = MyUserCreationForm
    list_display = ('email', 'username', 'date_joined', 'last_login', 'is_admin','is_staff')
    search_fields = ('email', 'first_name')
    readonly_fields=('date_joined', 'last_login', 'username')
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Notary)
admin.site.register(Appointment)
admin.site.register(User, AccountAdmin)
