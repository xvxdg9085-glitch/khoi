# users/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models.customuser import CustomUser
from .models.post import Post
from .models.product import Product, ProductCategory, ProductImage


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



@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "is_active", "created_at")
    search_fields = ("name",)
    list_filter = ("is_active", "created_at")


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "stock", "discount",
                    "category", "is_featured", "is_active")
    search_fields = ("name",)
    list_filter = ("category", "is_active", "is_featured")
    inlines = [ProductImageInline]
@admin.register(ProductImage)

class ProductImageAdmin(admin.ModelAdmin):
    list_display = ("product", "image", "uploaded_at", "is_active")

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_staff', 'is_active')
    search_fields = ('username', 'email')


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author')
    search_fields = ('title', 'content')
