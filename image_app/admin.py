from django.contrib import admin


from .models import ImageModel, MiniatureSize, ExpiringLink, ImageComment
from users_app.models import UserAccountTier, UserProfile

# Register your models here.

admin.site.register(ImageModel)
admin.site.register(MiniatureSize)
admin.site.register(ExpiringLink)
admin.site.register(ImageComment)


class MiniatureSizeInline(admin.StackedInline):
    model = UserAccountTier.mini_size.through


class ImageModelAdmin(admin.ModelAdmin):
    list_display = ['user', 'title', 'short_description', ]
    date_hierarchy = 'uploaded_at'
    ordering = ['uploaded_at', 'user', 'title']


class MiniatureSizeAdmin(admin.ModelAdmin):
    list_display = ['height', 'width']


class ExpiringLinkAdmin(admin.ModelAdmin):
    list_display = '__all__'
