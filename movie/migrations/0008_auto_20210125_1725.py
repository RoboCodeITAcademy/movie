# Generated by Django 3.1.5 on 2021-01-25 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0007_movie_home_poster'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='poster',
            field=models.ImageField(upload_to='movie/', verbose_name='Poster, default=182x268'),
        ),
    ]
