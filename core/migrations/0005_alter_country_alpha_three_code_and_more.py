# Generated by Django 5.0.4 on 2024-07-24 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_activity_post_payment_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='country',
            name='alpha_three_code',
            field=models.CharField(max_length=3, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='country',
            name='alpha_two_code',
            field=models.CharField(max_length=2, null=True, unique=True),
        ),
    ]
