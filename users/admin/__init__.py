from django.contrib import admin

from users.models import BlogUserProfile
from django.contrib.auth.admin import UserAdmin as AuthorUserAdmin
from django.contrib.auth.models import User

class BlogUserProfileInline(admin.TabularInline):
    model = BlogUserProfile
    verbose_name = 'UserProfile'
    verbose_name_plural = 'UserProfiles'
    extra = 0


class UserAdmin(AuthorUserAdmin):
    inlines = [
        BlogUserProfileInline
    ]

# Assign the new UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)