# Generated by Django 3.0.14 on 2023-05-09 21:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project_app', '0013_auto_20230509_2142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='booking',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='project_app.Booking'),
        ),
    ]
