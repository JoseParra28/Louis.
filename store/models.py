from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User



class Category(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        verbose_name_plural = 'categories' 

    def __str__(self):
        return self.name


    def get_absolute_url(self):
        return reverse('category-list', args=[self.slug])      

class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=200)
    brand = models.CharField(max_length=250, default='un_branded')
    description = models.TextField(max_length=350, blank=True)
    has_sizes = models.BooleanField(default=False, null=True, blank=True)
    digital = models.BooleanField(default=False,null=True, blank=True)
    slug = models.SlugField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    image = models.ImageField(upload_to='media/')      

    class Meta:
        verbose_name_plural = 'products' 

    def __str__(self):
        return self.name  


    def get_absolute_url(self):
        return reverse('product-info', args=[self.slug])  



class ReviewRating(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100, blank=True)
    review = models.TextField(max_length=500, blank=True)
    rating = models.FloatField()
    ip = models.CharField(max_length=20, blank=True)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.subject



