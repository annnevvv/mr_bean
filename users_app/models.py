from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.db.models.signals import pre_save
from django.dispatch import receiver


from image_app.models import MiniatureSize

# Create your models here.


class UserAccountTier(models.Model):
    name = models.CharField(max_length=50, unique=True)
    mini_size = models.ManyToManyField(MiniatureSize, null=True)
    ability_to_generate_custom_size_mini = models.BooleanField(default=0)
    presence_link_to_org_file = models.BooleanField(default=0)
    ability_to_generate_expiring_links = models.BooleanField(default=0)

    price = models.PositiveBigIntegerField(default=1)

    def __str__(self):
        return self.name


def user_avatar_image_path(instance, filename):

    return f'users/{instance.user.id}/avatar_{instance.user.id}{filename[-4:]}'


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    tier = models.ForeignKey(UserAccountTier,
                             on_delete=models.CASCADE,
                             default=1)
    avatar = models.ImageField(upload_to=user_avatar_image_path,
                               default='koteł.jpg')
    points = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.user.username}"


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()


# admn_user = User.objects.get(username='admn')
# user_profile = UserProfileModel.objects.create(user=admn_user)

# # user_profile.inne_pole = 'jakas_wartosc'
# user_profile.save()
