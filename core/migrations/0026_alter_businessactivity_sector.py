# Generated by Django 5.0.4 on 2024-07-31 13:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0025_remove_businessactivity_business_choice_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='businessactivity',
            name='sector',
            field=models.ForeignKey(default=('non', 'Non'), null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.sector', verbose_name="Domaine d'activité"),
        ),
    ]