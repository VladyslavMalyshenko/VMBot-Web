from django.contrib import admin

from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'discord_id']
    list_display_links = ['id', 'username', 'discord_id']
    search_fields = ['id', 'username', 'discord_id']

    fieldsets = (
        ('Global info', {'fields': ('username', 'last_login')}),
        ('Global info', {'fields': (
            'username_with_tag',
            'discord_id',
            'avatar',
            'is_active',
            'is_superuser',
            'is_staff'
        )})
    )
