from django.contrib import admin
from .models import *



class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'rating',
        'image',
        'brand',
        'description',
        'slug',
        
    )

ordering = ('sku',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'slug',
        'name',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(ReviewRating)


