# Generated by Django 5.0.8 on 2025-01-02 02:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('things', '0005_alter_thing_featured_alter_thing_internal_page_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='thing',
            name='image',
        ),
    ]
