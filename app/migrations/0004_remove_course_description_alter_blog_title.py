# Generated by Django 4.2.2 on 2023-07-21 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_feedback_group_course'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='description',
        ),
        migrations.AlterField(
            model_name='blog',
            name='title',
            field=models.CharField(max_length=30),
        ),
    ]
