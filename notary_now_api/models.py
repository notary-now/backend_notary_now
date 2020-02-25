from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from .utils import AppointmentStatuses
from uuid import uuid4

class MyUserManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, password = None):
        if not email:
            raise ValueError('Users must have an email address.')
        if not first_name:
            raise ValueError('Users must have a first name.')
        if not last_name:
            raise ValueError('Users must have a last name.')

        user = self.model(
            email = self.normalize_email(email),
            first_name = first_name.capitalize(),
            last_name = last_name.capitalize())

        user.set_password(password)

        user.save(using = self._db)

        return user

    def create_superuser(self, email, first_name, last_name, password):
        user = self.create_user(
            email = self.normalize_email(email),
            first_name = first_name.capitalize(),
            last_name = last_name.capitalize(),
            password = password)

        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True

        user.save(using = self._db)

        return user

class User(AbstractBaseUser):
    date_joined = models.DateTimeField(verbose_name = 'date joined', auto_now_add = True)
    last_login = models.DateTimeField(verbose_name = 'last login', auto_now = True)
    username = models.CharField(max_length = 50, default=uuid4().hex)
    is_admin = models.BooleanField(default = False)
    is_active = models.BooleanField(default = True)
    is_staff = models.BooleanField(default = False)
    is_superuser = models.BooleanField(default = False)
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    email = models.EmailField(unique = True)
    zip_code = models.PositiveIntegerField(default=80222)
    profile_photo = models.TextField(default = 'https://www.netclipart.com/pp/m/23-234697_blue-onesie-clipart-stick-figure-happy-face.png')
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = MyUserManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj = None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

class Appointment(models.Model):
    notary = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='self_user')
    appointee = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='referenced_user')
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    status = models.IntegerField(
        choices=AppointmentStatuses.choices(),
        default=AppointmentStatuses.PENDING,
    )

    class Meta:
        constraints = [
        models.UniqueConstraint(fields=['date', 'time', 'notary_id'], name='unique_notary_appointment'),
        models.UniqueConstraint(fields=['date', 'time', 'appointee_id'], name='unique_user_appointment')
        ]

    @property
    def get_appointment_result(self):
        return AppointmentStatuses(self.status).name.title()

    @property
    def related_notary(self):
        return self.notary

    @property
    def related_appointee(self):
        return self.appointee

class Notary(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='notary_user')
    radius = models.PositiveIntegerField()
    active = models.BooleanField(default=True)
    bio = models.TextField(default="", max_length=5000)
    verified = models.BooleanField(default=False)
    state_notary_number = models.CharField(max_length=12)
    commission_date = models.DateField()
    expiration_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def related_user(self):
        return self.user
