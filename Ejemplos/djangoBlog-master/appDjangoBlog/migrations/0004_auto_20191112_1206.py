# Generated by Django 2.2.6 on 2019-11-12 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appDjangoBlog', '0003_auto_20191112_1158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='appDjangoBlog/static/img', verbose_name='Image'),
        ),
    ]
