# Generated by Django 3.0.4 on 2020-03-17 03:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tasks',
            old_name='createdAt',
            new_name='created_at',
        ),
    ]
