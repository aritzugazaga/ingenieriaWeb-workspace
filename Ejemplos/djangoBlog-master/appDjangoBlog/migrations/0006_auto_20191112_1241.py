# Generated by Django 2.2.6 on 2019-11-12 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appDjangoBlog', '0005_auto_20191112_1241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='img', verbose_name='Image'),
        ),
    ]
