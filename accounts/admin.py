#accounts/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUSerCreationForm, CustomUSerChangeForm
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    add_form = CustomUSerCreationForm
    form = CustomUSerChangeForm
    model = CustomUser

    list_display = ["username", "email", "is_staff"]

admin.site.register(CustomUser, CustomUserAdmin)