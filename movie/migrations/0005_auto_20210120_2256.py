# Generated by Django 3.1.5 on 2021-01-20 17:56

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('movie', '0004_auto_20210118_1615'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='dislikes',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='likes',
        ),
        migrations.AddField(
            model_name='movie',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='likes', to=settings.AUTH_USER_MODEL),
        ),
    ]
