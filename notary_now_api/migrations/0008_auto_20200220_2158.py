# Generated by Django 3.0.3 on 2020-02-20 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notary_now_api', '0007_auto_20200220_2136'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='appointment',
            constraint=models.UniqueConstraint(fields=('date', 'time', 'notary_id'), name='unique_appointment'),
        ),
    ]
