# Generated by Django 5.0.8 on 2024-12-30 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('things', '0003_alter_thing_city_alter_thing_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thing',
            name='featured',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='thing',
            name='internal_page',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]