# Generated by Django 5.0.6 on 2024-08-12 02:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website_app', '0010_schedulefile_remove_schedule_result_pdf_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ScheduleFile',
            new_name='ResultPdf',
        ),
    ]