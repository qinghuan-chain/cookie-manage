# Generated by Django 2.1.7 on 2021-08-08 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cookie', '0004_auto_20210804_0033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activerecordmodel',
            name='opera',
            field=models.CharField(blank=True, default='', max_length=128, null=True, verbose_name='操作'),
        ),
    ]
