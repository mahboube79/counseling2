# Generated by Django 4.2.4 on 2023-08-29 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_blog_main_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='blog_summery',
            field=models.TextField(max_length=200, verbose_name='خلاصه مقاله'),
        ),
    ]
