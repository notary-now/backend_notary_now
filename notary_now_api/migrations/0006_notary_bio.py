# Generated by Django 3.0.3 on 2020-02-19 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notary_now_api', '0005_remove_notary_bio'),
    ]

    operations = [
        migrations.AddField(
            model_name='notary',
            name='bio',
            field=models.TextField(default='', max_length=5000),
        ),
    ]
