# Generated by Django 3.0.6 on 2020-05-30 09:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posting', '0002_auto_20200527_2053'),
    ]

    operations = [
        migrations.AddField(
            model_name='my_post',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='tag',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='my_post',
            name='my_post_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 30, 12, 16, 14, 616641)),
        ),
    ]