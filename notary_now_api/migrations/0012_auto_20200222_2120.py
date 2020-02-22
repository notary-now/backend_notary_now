# Generated by Django 3.0.3 on 2020-02-22 21:20

from django.db import migrations, models
import notary_now_api.utils


class Migration(migrations.Migration):

    dependencies = [
        ('notary_now_api', '0011_appointment_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='status',
            field=models.IntegerField(choices=[(1, 'PENDING'), (2, 'COMPLETED'), (3, 'CANCELLED')], default=notary_now_api.utils.AppointmentStatuses['PENDING']),
        ),
    ]