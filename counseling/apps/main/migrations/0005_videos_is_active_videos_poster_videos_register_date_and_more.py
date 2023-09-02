# Generated by Django 4.2.4 on 2023-08-30 23:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0004_alter_blog_blog_summery'),
    ]

    operations = [
        migrations.AddField(
            model_name='videos',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='videos',
            name='poster',
            field=models.ImageField(default=None, upload_to='images/blogimg/', verbose_name='پوستر ویدئو'),
        ),
        migrations.AddField(
            model_name='videos',
            name='register_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='videos',
            name='user_registered',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='videos',
            name='video',
            field=models.FileField(upload_to='video/videos/', verbose_name='ویدئو'),
        ),
    ]
