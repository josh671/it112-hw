# Generated by Django 3.1.7 on 2021-05-28 03:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Club', '0009_auto_20210527_1926'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='meetingminutes',
            name='Attendance',
        ),
    ]