# Generated by Django 4.2.9 on 2024-01-06 16:38

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('image_app', '0003_alter_imagecommentmodel_text'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ImageCommentModel',
            new_name='ImageComment',
        ),
    ]