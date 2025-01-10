from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from unfold.admin import ModelAdmin
from .models import User
from django.urls import reverse
from django.utils.html import format_html
from unfold.forms import AdminPasswordChangeForm, UserChangeForm, UserCreationForm


@admin.register(User)
class UserAdmin(UserAdmin, ModelAdmin):
    list_display = ('username', 'email', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active')

    form = UserChangeForm  # Form used when updating a user
    add_form = UserCreationForm  # Form used when creating a new user
    change_password_form = AdminPasswordChangeForm  # Form for password change

    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'is_staff', 'is_active')}
        ),
    )

    search_fields = ('username', 'email')
    ordering = ('username',)

    def get_form(self, request, obj=None, **kwargs):
        if obj is None:  
            kwargs['form'] = self.add_form  
        else:
            kwargs['form'] = self.form  
        return super().get_form(request, obj, **kwargs)

    def get_fieldsets(self, request, obj=None):
        if obj is None:
            return self.add_fieldsets  
        return self.fieldsets  
