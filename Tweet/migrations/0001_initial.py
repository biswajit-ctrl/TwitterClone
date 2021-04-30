# Generated by Django 3.2 on 2021-04-30 11:51

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tweet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Name')),
                ('body', models.TextField(max_length=200, verbose_name='Caption')),
                ('image', cloudinary.models.CloudinaryField(blank=True, max_length=255, verbose_name='Image')),
                ('like_count', models.IntegerField(blank=True, default=0, verbose_name='Total counts of Like')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('hidden', models.BooleanField(default=False)),
            ],
        ),
    ]
