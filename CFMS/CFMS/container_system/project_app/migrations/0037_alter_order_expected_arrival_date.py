# Generated by Django 4.2.3 on 2023-12-04 05:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_app', '0036_remove_user_user_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='expected_arrival_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 13, 5, 33, 23, 724126)),
        ),
    ]
