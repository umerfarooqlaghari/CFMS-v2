# Generated by Django 3.0.14 on 2023-05-07 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_app', '0003_auto_20230507_1706'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faq',
            name='user_email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='faq',
            name='user_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
