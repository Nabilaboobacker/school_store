# Generated by Django 5.0.1 on 2024-02-04 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store_app', '0002_user_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_profile',
            name='email',
            field=models.EmailField(default='admin1@gmail.com', max_length=100),
        ),
    ]