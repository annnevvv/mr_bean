from django.contrib import admin


from .models import ImageModel, MiniatureSizeModel, ExpiringLinkModel, ImageCommentModel
from users_app.models import UserAccountTier, UserProfileModel

# Register your models here.

admin.site.register(ImageModel)
admin.site.register(MiniatureSizeModel)
admin.site.register(ExpiringLinkModel)
admin.site.register(ImageCommentModel)


class MiniatureSizeInline(admin.StackedInline):
    model = UserAccountTier.mini_size.through


class SendedImageAdmin(admin.ModelAdmin):
    list_display = ['user', 'title', 'short_description', ]
    date_hierarchy = 'uploaded_at'
    ordering = ['uploaded_at', 'user', 'title']


class MiniatureSizeAdmin(admin.ModelAdmin):
    list_display = ['height', 'width']


class ExpiringLinkAdmin(admin.ModelAdmin):
    list_display = '__all__'
