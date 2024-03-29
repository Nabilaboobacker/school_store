# Generated by Django 5.0.1 on 2024-02-04 14:10

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store_app', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='User_profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('date_of_birth', models.DateField()),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=1)),
                ('phone', models.CharField(max_length=15)),
                ('address', models.TextField()),
                ('purpose', models.CharField(choices=[('order', 'Place Order'), ('enquiry', 'Enquiry'), ('return', 'Return')], max_length=10)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store_app.course')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store_app.department')),
                ('materials_provide', models.ManyToManyField(to='store_app.material')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
