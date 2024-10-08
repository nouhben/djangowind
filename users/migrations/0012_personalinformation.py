# Generated by Django 5.0.4 on 2024-07-18 14:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_alter_customuser_business_address_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='PersonalInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('birth_country', models.CharField(blank=True, default='France', max_length=100)),
                ('birth_place', models.TextField(blank=True)),
                ('birth_date', models.DateField(blank=True, default=datetime.date(1990, 1, 1))),
                ('sex', models.CharField(blank=True, default='Man', max_length=20)),
            ],
        ),
    ]
