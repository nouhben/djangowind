# Generated by Django 5.0.4 on 2024-07-24 22:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0023_alter_businessactivity_business_choice_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='businessactivity',
            name='is_micro',
            field=models.BooleanField(blank=True, choices=[(None, 'Non'), (False, 'Oui, En tant que EURL, SARL, SASU, SAS, etc.'), (True, 'Oui, En tant que micro-entreprise / entrepreneur individuel')], default=None, null=True, verbose_name='Avez-vous déjà exercé une activité non-salariée ?'),
        ),
    ]
