# Generated by Django 4.2.3 on 2023-12-04 04:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_app', '0035_userprofile_address_userprofile_cell_phone_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='user_type',
        ),
        migrations.AlterField(
            model_name='order',
            name='expected_arrival_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 13, 4, 37, 24, 637389)),
        ),
    ]
