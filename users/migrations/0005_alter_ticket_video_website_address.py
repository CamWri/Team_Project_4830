# Generated by Django 5.0.3 on 2024-04-04 19:27

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_ticket_video_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='video_website_address',
            field=models.URLField(blank=True, null=True, validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['mp4'])], verbose_name='Video Adress'),
        ),
    ]
