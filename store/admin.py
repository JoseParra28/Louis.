from django.contrib import admin
from .models import Product, Category


class CategoryAdmin(admin.ModelAdmin):
     list_display = (
         'name',
        'slug',
    )


admin.site.register(Category, CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'tittle',
        'category',
        'price',
        'description',
        'image',
        'slug',
    )

admin.site.register(Product, ProductAdmin)


