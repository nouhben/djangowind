# Generated by Django 5.0.4 on 2024-07-18 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_personalinformation'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='personalinformation',
            name='sex',
        ),
        migrations.AddField(
            model_name='personalinformation',
            name='gender',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]