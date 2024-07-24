# Generated by Django 5.0.4 on 2024-07-24 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_alter_activity_to_be_reviewed_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='activity',
            options={'verbose_name': 'Activity', 'verbose_name_plural': 'Activities'},
        ),
        migrations.AlterField(
            model_name='activity',
            name='connector_activity_id',
            field=models.CharField(blank=True, max_length=16, null=True, verbose_name='Connector Activity ID'),
        ),
        migrations.AlterField(
            model_name='activity',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='activity',
            name='has_children',
            field=models.BooleanField(default=False, verbose_name='Has Children'),
        ),
        migrations.AlterField(
            model_name='activity',
            name='jqpa',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='JQPA'),
        ),
        migrations.AlterField(
            model_name='activity',
            name='name',
            field=models.CharField(default='Autre', max_length=256, unique=True, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='activity',
            name='post_payment',
            field=models.SmallIntegerField(blank=True, null=True, verbose_name='Post Payment'),
        ),
        migrations.AlterField(
            model_name='activity',
            name='sub_id',
            field=models.IntegerField(default=0, unique=True, verbose_name='Sub ID'),
        ),
        migrations.AlterField(
            model_name='activity',
            name='to_be_reviewed',
            field=models.BooleanField(default=False, verbose_name='To Be Reviewed'),
        ),
        migrations.AlterField(
            model_name='activity',
            name='type',
            field=models.CharField(blank=True, choices=[('commercial', 'Commercial'), ('non-commercial', 'Non-Commercial')], max_length=64, null=True, verbose_name='Type'),
        ),
        migrations.AddIndex(
            model_name='activity',
            index=models.Index(fields=['sub_id'], name='core_activi_sub_id_b731ae_idx'),
        ),
        migrations.AddIndex(
            model_name='activity',
            index=models.Index(fields=['name'], name='core_activi_name_d6f9ca_idx'),
        ),
    ]
