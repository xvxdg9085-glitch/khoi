from django.db import models
from ckeditor.fields import RichTextField

class ProductCategory(models.Model):
    """Product category table"""
    name = models.CharField(max_length=255, unique=True,
                            verbose_name="Category name")
    description = models.TextField(
        blank=True, null=True, verbose_name="Category description")
    thumbnail = models.ImageField(
        upload_to='category_thumbnails/', blank=True, null=True, verbose_name="Thumbnail")
    is_active = models.BooleanField(default=True, verbose_name="Active")
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Created at")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated at")

    class Meta:
        verbose_name = "Product category"
        verbose_name_plural = "Product categories"

    def __str__(self):
        return self.name

    @property
    def discounted_price(self):
        if self.discount:
            return self.price * (100 - self.discount) / 100
        return self.price
class Product(models.Model):
    """Product detail table"""
    name = models.CharField(max_length=255, verbose_name="Product name")
    price = models.DecimalField(
        max_digits=12, decimal_places=2, verbose_name="Price")
    stock = models.PositiveIntegerField(
        default=0, verbose_name="Stock quantity")
    discount = models.DecimalField(
        max_digits=5, decimal_places=2, default=0, verbose_name="Discount (%)")
    main_image = models.ImageField(
        upload_to='product_images/', verbose_name="Main image")
    category = models.ForeignKey(
        ProductCategory, on_delete=models.CASCADE, related_name='products', verbose_name="Category")
    description = RichTextField(verbose_name="Product description")
    is_featured = models.BooleanField(default=False, verbose_name="Featured")
    is_active = models.BooleanField(default=True, verbose_name="Active")
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Created at")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated at")

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def __str__(self):
        return self.name

    @property
    def discounted_price(self):
        if self.discount:
            return self.price * (100 - self.discount) / 100
        return self.price


class ProductImage(models.Model):
    """Additional product images"""
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='images', verbose_name="Product")
    image = models.ImageField(
        upload_to='static/product_images/', verbose_name="Image")
    is_active = models.BooleanField(default=True, verbose_name="Active")
    uploaded_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Uploaded at")

    class Meta:
        verbose_name = "Product image"
        verbose_name_plural = "Product images"

    def __str__(self):
        return f"Image of {self.product.name}"
