# Generated by Django 2.2.7 on 2019-12-06 07:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('volunteer', '0004_auto_20191206_0553'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='volunteerregistration',
            name='skills',
        ),
    ]
