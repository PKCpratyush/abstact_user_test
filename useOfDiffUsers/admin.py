from django.contrib import admin
from django.contrib.auth.models import User
from useOfDiffUsers.models import New_user
from django.contrib.auth.admin import UserAdmin

# Register your models here.

# admin.site.register(New_user)

# customizing the admin panel

class UserAdminConfig(UserAdmin):
    search_fields = ('user_name',)
    ordering = ('-user_name',)
    list_display = ('user_name','password','is_active','is_staff')

    # adding fields and making diffrent parts
    fieldsets = (
        (None, {'fields':('user_name','password')}),
        ('Permissions',{'fields':('is_staff','is_active')})
    )

    add_fieldsets = (
        (None,{
            'classes':('wide',),
            'fields':('user_name','password','is_staff','is_active')
        }),
    )


admin.site.register(New_user, UserAdminConfig)