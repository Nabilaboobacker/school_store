# Generated by Django 5.0.1 on 2024-02-05 04:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store_app', '0006_remove_user_profile_age'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_profile',
            name='age',
            field=models.PositiveIntegerField(blank=True, default=0),
        ),
    ]
