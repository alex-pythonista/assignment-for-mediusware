from django.contrib import admin

from .models import (
    Product,
    ProductVariant,
    ProductImage,
    ProductVariantPrice,
    Variant,
)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'sku']


@admin.register(ProductVariant)
class ProductVariantAdmin(admin.ModelAdmin):
    list_display = ['variant_title']


@admin.register(ProductVariantPrice)
class ProductVariantPriceAdmin(admin.ModelAdmin):
    list_display = [
        'product', 
        'product_variant_one', 
        'product_variant_two',
        'product_variant_three',
        'price', 'stock']


@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ['product', 'file_path']


@admin.register(Variant)
class VariantAdmin(admin.ModelAdmin):
    list_display = ['title', 'active']