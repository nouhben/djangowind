# Generated by Django 5.0.4 on 2024-08-02 12:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0028_alter_businessactivity_activity_type_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='BusinessAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street_address', models.CharField(blank=True, max_length=255, null=True)),
                ('postal_code', models.CharField(blank=True, db_index=True, max_length=20, null=True)),
                ('city', models.CharField(blank=True, max_length=100, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_verified', models.BooleanField(default=False)),
                ('country', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.country')),
            ],
            options={
                'verbose_name_plural': 'Addresses',
                'indexes': [models.Index(fields=['postal_code', 'city'], name='core_busine_postal__1d2388_idx')],
            },
        ),
    ]
