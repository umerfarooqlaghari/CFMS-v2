# Generated by Django 3.0.14 on 2023-05-10 01:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_app', '0023_auto_20230510_0008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='expected_arrival_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 19, 1, 0, 40, 160377)),
        ),
    ]
