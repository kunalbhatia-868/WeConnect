# Generated by Django 3.2.8 on 2021-10-26 18:34

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Friends',
            new_name='Friend',
        ),
    ]
