# Generated by Django 5.0.6 on 2024-05-23 12:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Member',
            new_name='Members',
        ),
    ]