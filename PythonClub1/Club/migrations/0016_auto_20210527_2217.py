# Generated by Django 3.1.7 on 2021-05-28 05:17

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Club', '0015_auto_20210527_2211'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='meetingminutes',
            name='Attendance',
        ),
        migrations.AddField(
            model_name='meetingminutes',
            name='Attendance',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
