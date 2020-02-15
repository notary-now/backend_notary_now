from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    email = models.EmailField(max_length=100)
    bio = models.TextField(max_length=5000)
    noatry_id = models.PositiveIntegerField()
    commission_date = models.DateField()
    expiration_date = models.DateField()
    verified = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Location(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    zip_code = models.PositiveIntegerField()
    radius = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Appointment(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE, related_name='self_user')
    apointee = models.ForeignKey('User', on_delete=models.CASCADE, related_name='referenced_user')
    time = models.DateTimeField()
    location = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Language(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    primary_language = models.CharField(max_length=1000)
    secondary_language = models.CharField(max_length=1000)
    tertiary_language = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)