# Generated by Django 2.1.7 on 2019-05-28 02:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0004_course_update_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='about',
        ),
        migrations.RemoveField(
            model_name='course',
            name='update_at',
        ),
    ]
