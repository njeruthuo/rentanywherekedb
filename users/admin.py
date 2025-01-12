from django.contrib import admin

from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'username', 'is_active')
    search_fields = ('email', 'username')
    list_filter = ('is_active', 'is_staff')
