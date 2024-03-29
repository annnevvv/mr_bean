from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.core.validators import MinValueValidator, MinLengthValidator, MaxValueValidator, MaxLengthValidator


def user_uploaded_image_path(instance, filename):
    return f'users/{instance.user.id}/uploaded_img/{filename}'


class ImageModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    image_file = models.ImageField(upload_to=user_uploaded_image_path,
                                   blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    short_description = models.TextField(max_length=300, null=True, blank=True)
    private = models.BooleanField(default=True)
    beans = models.PositiveIntegerField(default=3)
    users_likes = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name='images_liked', blank=True)

    # class Meta:
    #     indexes = [
    #         models.Index(fields=['-updated_date']),
    #         models.Index(fields=['-users_likes']),
    #     ]
    #     ordering = ['uploaded_at']

    # db_table = ''
    # managed = True
    # verbose_name = 'ModelName'
    # verbose_name_plural = 'ModelNames'

    def __str__(self):
        return self.title


class ImageComment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    img = models.ForeignKey(ImageModel, on_delete=models.CASCADE)
    published_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    text = models.TextField(validators=[
        MinLengthValidator(
            limit_value=30, message="The text must contain at least 30 characters."),
        MaxLengthValidator(
            limit_value=3000, message="The text cannot exceed 3000 characters."),
    ]
    )


class MiniatureSize(models.Model):
    height = models.PositiveIntegerField()
    width = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.height}x{self.width}'


class ExpiringLink(models.Model):
    name = models.CharField(max_length=30, unique=True, null=True)
    creation_time = models.DateTimeField(auto_now_add=True)
    expiration = models.PositiveIntegerField(
        validators=[MinValueValidator(300), MaxValueValidator(3000)],
        default=3000)
    img = models.OneToOneField(ImageModel, on_delete=models.CASCADE,
                               null=True, blank=True)
