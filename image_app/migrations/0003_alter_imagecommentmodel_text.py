# Generated by Django 4.2.9 on 2024-01-06 16:37

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('image_app', '0002_rename_txt_imagecommentmodel_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagecommentmodel',
            name='text',
            field=models.TextField(validators=[django.core.validators.MinValueValidator(limit_value=30, message='The text must contain at least 30 characters.'), django.core.validators.MaxValueValidator(limit_value=3000, message='The text cannot exceed 3000 characters.')]),
        ),
    ]
