# Generated by Django 3.0.14 on 2023-05-08 10:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project_app', '0008_auto_20230507_2204'),
    ]

    operations = [
        migrations.RenameField(
            model_name='faq',
            old_name='question',
            new_name='query',
        ),
        migrations.RemoveField(
            model_name='faq',
            name='answer',
        ),
    ]
