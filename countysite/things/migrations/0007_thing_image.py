# Generated by Django 5.0.8 on 2025-01-02 02:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('things', '0006_remove_thing_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='thing',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='thing_img/'),
        ),
    ]