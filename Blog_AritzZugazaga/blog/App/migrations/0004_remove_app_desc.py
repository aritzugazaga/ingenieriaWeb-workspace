# Generated by Django 3.1.2 on 2020-10-14 07:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0003_app_desc'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='app',
            name='desc',
        ),
    ]
