# Generated by Django 4.1.2 on 2022-12-07 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0004_remove_attendance_time_out'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendance',
            name='timed_out',
            field=models.CharField(default='no', max_length=10),
        ),
    ]