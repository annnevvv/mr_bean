from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator


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

    def __str__(self):
        return self.title


class ImageCommentModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    img = models.ForeignKey(ImageModel, on_delete=models.CASCADE)
    published_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    txt = models.TextField([MinValueValidator(30), MaxValueValidator(3000)])


class MiniatureSizeModel(models.Model):
    height = models.PositiveIntegerField()
    width = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.height}x{self.width}'


class ExpiringLinkModel(models.Model):
    name = models.CharField(max_length=30, unique=True, null=True)
    creation_time = models.DateTimeField(auto_now_add=True)
    expiration = models.PositiveIntegerField(
        validators=[MinValueValidator(300), MaxValueValidator(3000)],
        default=3000)
    img = models.OneToOneField(ImageModel, on_delete=models.CASCADE,
                               null=True, blank=True)
