# Generated by Django 5.0.6 on 2024-08-09 00:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website_app', '0006_remove_schedule_date_schedule_end_schedule_start'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='result',
            field=models.TextField(default='', verbose_name='リザルト'),
        ),
    ]
