# Generated by Django 5.0.1 on 2024-04-19 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0002_extralinks_enabled_store_enabled_alter_profile_about_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='extralinks',
            name='position',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]