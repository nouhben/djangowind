# Generated by Django 5.0.4 on 2024-07-23 21:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_id', models.IntegerField(null=True, unique=True)),
                ('name', models.CharField(max_length=256, unique=True)),
                ('description', models.TextField(blank=True)),
                ('connector_activity_id', models.CharField(max_length=16, null=True)),
                ('has_children', models.BooleanField(default=True)),
                ('to_be_reviewed', models.BooleanField(default=False)),
                ('type', models.CharField(max_length=64, null=True)),
                ('jqpa', models.CharField(max_length=64, null=True)),
                ('post_payment', models.IntegerField(max_length=6, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, unique=True)),
                ('code', models.IntegerField(max_length=6, unique=True)),
                ('alpha_two_code', models.CharField(max_length=2, unique=True)),
                ('alpha_three_code', models.CharField(max_length=3, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='ActivitySector',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_id', models.IntegerField(null=True, unique=True)),
                ('name', models.CharField(max_length=256, unique=True)),
                ('description', models.TextField(blank=True)),
                ('connector_activity_id', models.CharField(max_length=16, null=True)),
                ('has_children', models.BooleanField(default=False)),
                ('to_be_reviewed', models.BooleanField(default=False)),
                ('type', models.CharField(max_length=64, null=True)),
                ('jqpa', models.CharField(max_length=64, null=True)),
                ('post_payment', models.IntegerField(max_length=6, null=True)),
                ('parent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.activity')),
            ],
        ),
    ]
