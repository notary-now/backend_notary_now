# Generated by Django 3.0.3 on 2020-02-25 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notary_now_api', '0015_auto_20200225_1908'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(default='8bf948862296483eb6dd895843c8ec3e', max_length=50, unique=True),
        ),
    ]
