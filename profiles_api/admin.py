from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, FeedItem

# Register your models here.


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    ...


@admin.register(FeedItem)
class FeedItemAdmin(admin.ModelAdmin):
    list_display = ('user_profile', 'status_text', 'created_on')
