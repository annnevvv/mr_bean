# Generated by Django 4.2.1 on 2023-11-22 23:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import users_app.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('image_app', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserAccountTier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('presence_link_to_org_file', models.BooleanField(default=0)),
                ('ability_to_generate_expiring_links', models.BooleanField(default=0)),
                ('mini_size', models.ManyToManyField(null=True, to='image_app.miniaturesizemodel')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfileModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(default='koteł.jpg', upload_to=users_app.models.user_avatar_image_path)),
                ('points', models.IntegerField(default=0)),
                ('tier', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='users_app.useraccounttier')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]