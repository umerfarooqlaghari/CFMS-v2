# Generated by Django 3.0.14 on 2023-05-09 22:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('project_app', '0014_auto_20230509_2158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userlog',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
