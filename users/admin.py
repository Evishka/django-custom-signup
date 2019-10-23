from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User, Group
from django.contrib.sites.models import Site

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (None, {
            'fields': ('email', 'personal_url', 'first_name', 'last_name','password')
        }),)
    list_display = ['email', 'personal_url','first_name','last_name',]
    search_fields = ['email', 'personal_url','first_name','last_name',]
    
admin.site.unregister(Group)
admin.site.unregister(Site)
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.site_header = 'Administration'