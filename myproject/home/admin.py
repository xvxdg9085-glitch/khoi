# users/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models.customuser import CustomUser
from .models.post import Post

admin.site.register(Post)


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('email', 'full_name', 'phone_number', 'is_customer')
    list_filter = ('is_customer', 'gender')
    ordering = ('email',)

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('full_name', 'phone_number',
         'gender', 'date_of_birth', 'address_1', 'address_2')}),
        ('Permissions', {'fields': ('is_customer', 'is_active',
         'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'full_name', 'phone_number', 'password1', 'password2', 'is_customer')}
         ),
    )


admin.site.register(CustomUser, CustomUserAdmin)
