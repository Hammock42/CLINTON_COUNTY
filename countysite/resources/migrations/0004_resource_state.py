# Generated by Django 5.0.8 on 2025-01-01 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0003_alter_resource_city'),
    ]

    operations = [
        migrations.AddField(
            model_name='resource',
            name='state',
            field=models.CharField(default='MO', max_length=2),
        ),
    ]
