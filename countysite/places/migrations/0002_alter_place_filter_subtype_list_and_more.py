# Generated by Django 5.0.8 on 2024-12-30 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0001_initial'),
        ('things', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='filter_subtype_list',
            field=models.ManyToManyField(blank=True, related_name='place_subtype_filters', to='things.filtersubtype'),
        ),
        migrations.AlterField(
            model_name='place',
            name='filter_type_list',
            field=models.ManyToManyField(blank=True, related_name='place_type_filters', to='things.filtertype'),
        ),
    ]
