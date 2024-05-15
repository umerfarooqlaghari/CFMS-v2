# Generated by Django 3.0.14 on 2023-05-07 22:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('project_app', '0007_auto_20230507_2155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='booking_email_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='email_address', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='booking',
            name='booking_phone',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_phone', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
