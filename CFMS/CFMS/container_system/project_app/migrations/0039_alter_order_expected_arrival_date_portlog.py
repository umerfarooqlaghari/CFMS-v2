# Generated by Django 4.2.3 on 2023-12-07 09:43

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project_app', '0038_alter_order_expected_arrival_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='expected_arrival_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 16, 9, 43, 7, 500493)),
        ),
        migrations.CreateModel(
            name='PortLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('Port_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project_app.port')),
            ],
        ),
    ]
