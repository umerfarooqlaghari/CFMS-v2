# Generated by Django 4.2.3 on 2023-12-07 09:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_app', '0037_alter_order_expected_arrival_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='expected_arrival_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 16, 9, 8, 23, 841480)),
        ),
    ]