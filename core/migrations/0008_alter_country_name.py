# Generated by Django 5.0.4 on 2024-07-24 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_alter_country_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='country',
            name='name',
            field=models.CharField(blank=True, max_length=256),
        ),
    ]
