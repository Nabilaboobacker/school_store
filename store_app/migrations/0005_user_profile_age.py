# Generated by Django 5.0.1 on 2024-02-04 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store_app', '0004_alter_user_profile_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_profile',
            name='age',
            field=models.PositiveIntegerField(blank=True, default=0),
        ),
    ]