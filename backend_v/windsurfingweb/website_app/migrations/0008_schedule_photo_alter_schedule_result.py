# Generated by Django 5.0.6 on 2024-08-09 00:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website_app', '0007_alter_schedule_result'),
    ]

    operations = [
        migrations.AddField(
            model_name='schedule',
            name='photo',
            field=models.ImageField(blank=True, upload_to='photos/'),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='result',
            field=models.TextField(blank=True, verbose_name='リザルト'),
        ),
    ]