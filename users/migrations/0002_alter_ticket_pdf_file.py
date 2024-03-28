# Generated by Django 5.0.3 on 2024-03-28 00:18

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='pdf_file',
            field=models.FileField(blank=True, null=True, upload_to='', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf', 'doc'])], verbose_name='PDF File'),
        ),
    ]
