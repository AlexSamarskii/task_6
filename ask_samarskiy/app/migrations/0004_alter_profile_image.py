# Generated by Django 4.2.17 on 2024-12-24 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='profile.jpg', upload_to='static/img/'),
        ),
    ]