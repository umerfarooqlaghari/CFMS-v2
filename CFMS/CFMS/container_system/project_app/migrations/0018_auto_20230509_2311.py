# Generated by Django 3.0.14 on 2023-05-09 23:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_app', '0017_auto_20230509_2233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='expected_arrival_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 18, 23, 11, 43, 387451)),
        ),
    ]