# Generated by Django 3.0.3 on 2020-02-19 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notary_now_api', '0002_auto_20200219_0101'),
    ]

    operations = [
        migrations.AddField(
            model_name='notary',
            name='bio',
            field=models.TextField(default='Hi Im david', max_length=5000),
            preserve_default=False,
        ),
    ]
