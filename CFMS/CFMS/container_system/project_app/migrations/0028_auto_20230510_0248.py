# Generated by Django 3.0.14 on 2023-05-10 02:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_app', '0027_auto_20230510_0243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='expected_arrival_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 19, 2, 48, 48, 252864)),
        ),
    ]
