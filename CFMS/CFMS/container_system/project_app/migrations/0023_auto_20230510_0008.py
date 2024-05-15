# Generated by Django 3.0.14 on 2023-05-10 00:08

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project_app', '0022_auto_20230510_0007'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='tax',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='project_app.CostCalculation'),
        ),
        migrations.AlterField(
            model_name='order',
            name='expected_arrival_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 19, 0, 8, 47, 207534)),
        ),
    ]