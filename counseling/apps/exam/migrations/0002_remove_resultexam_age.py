# Generated by Django 4.2.4 on 2023-08-25 16:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resultexam',
            name='age',
        ),
    ]
