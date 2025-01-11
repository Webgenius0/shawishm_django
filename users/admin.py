from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin, GroupAdmin
from unfold.admin import ModelAdmin
from .models import User
from unfold.forms import AdminPasswordChangeForm, UserChangeForm, UserCreationForm



admin.site.unregister(Group)
@admin.register(User)
class UserAdmin(UserAdmin, ModelAdmin ):
    list_display = ('id', 'U_ID', 'username', 'U_fullname', 'U_sex', 'U_address', 'U_Role', 'U_phone', 'password', 'RG_ID', 'is_staff', 'is_active' , 'date_joined', 'created_at', 'updated_at')
    list_filter = ('is_staff', 'is_active')

    form = UserChangeForm
    add_form = UserCreationForm
    change_password_form = AdminPasswordChangeForm

    fieldsets = (
        (None, {'fields': ('U_ID', 'username', 'U_fullname', 'U_sex', 'U_address', 'U_Role', 'U_phone', 'password', 'RG_ID')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('date_joined', 'last_login',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ( 'U_ID', 'username', 'U_fullname', 'U_sex', 'U_address', 'U_Role', 'U_phone', 'password', 'RG_ID')}
        ),
    )

    search_fields = ('username', 'id')
    ordering = ('username','id')
    exclude = ('created_at', 'updated_at')

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

@admin.register(Group)
class GroupAdmin(GroupAdmin, ModelAdmin):
    pass