# Generated by Django 2.1.7 on 2021-08-11 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cookie', '0005_auto_20210808_1546'),
    ]

    operations = [
        migrations.AddField(
            model_name='accountmodel',
            name='opera_datetime',
            field=models.DateTimeField(auto_now=True, verbose_name='操作时间'),
        ),
    ]
