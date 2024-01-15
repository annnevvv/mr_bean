from django.contrib import admin

from image_app.admin import MiniatureSizeInline


from .models import UserAccountTier, UserProfile, User

# Register your models here.

admin.site.register(UserAccountTier)
admin.site.register(UserProfile)


class UserAccountTierAdmin(admin.ModelAdmin):
    inlines = [MiniatureSizeInline]
    list_display = ['name', ]
    search_fields = ['name', ]


class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False


class UserAdmin(admin.ModelAdmin):
    inlines = (UserProfileInline,)


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
