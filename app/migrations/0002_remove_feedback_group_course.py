# Generated by Django 4.2.2 on 2023-07-14 06:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feedback',
            name='group_course',
        ),
    ]
