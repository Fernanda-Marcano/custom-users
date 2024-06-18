from django.contrib import admin
from .models import CustomUser, ProfileUser

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_active', 'is_admin')
    list_filter = ('is_active', 'is_admin')
    search_fields = ('username', 'email', 'is_active', 'is_admin')

admin.site.register(CustomUser, CustomUserAdmin)


class ProfileUserAdmin(admin.ModelAdmin):
    list_display = ('dni', 'birthdate', 'address', 'telephone')
    list_filter = ('dni', 'birthdate')
    search_fields = ('dni', 'birthdate', 'telephone')
    date_hierarchy = 'birthdate'

admin.site.register(ProfileUser, ProfileUserAdmin)