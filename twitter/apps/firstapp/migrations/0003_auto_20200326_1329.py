# Generated by Django 3.0.4 on 2020-03-26 10:29

from django.db import migrations, models
import firstapp.models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0002_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, default='', upload_to=firstapp.models.user_directory_path),
        ),
    ]