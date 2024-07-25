# Generated by Django 5.0.4 on 2024-07-24 20:06

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0021_alter_businessactivity_sector_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='businessactivity',
            name='business_choice',
            field=models.CharField(choices=[('NON', 'Non'), ('OUI', 'Oui'), ('OUI', 'Oui')], default='Non', max_length=64, verbose_name='Avez-vous déjà exercé une activité non-salariée ?'),
        ),
        migrations.AlterField(
            model_name='businessactivity',
            name='sector',
            field=models.ForeignKey(default='Autre', null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.sector', verbose_name="Domaine d'activité"),
        ),
        migrations.AlterField(
            model_name='businessactivity',
            name='sub_sector',
            field=models.ForeignKey(default='Autre', null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.subsector', verbose_name="Secteur d'activité"),
        ),
        migrations.AlterField(
            model_name='businessactivity',
            name='when_to_start',
            field=models.DateField(default=datetime.date.today, null=True, verbose_name='Quand souhaitez-vous débuter votre activité ?'),
        ),
    ]