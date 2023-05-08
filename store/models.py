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
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.CASCADE)
    tittle = models.CharField(max_length=200)
    brand = models.CharField(max_length=250, default='un_branded')
    description = models.TextField(max_length=250, blank=True)
    slug = models.SlugField(max_length=255)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    image = models.ImageField(upload_to='media/')      

    class Meta:
        verbose_name_plural = 'products' 

    def __str__(self):
        return self.tittle  


    def get_absolute_url(self):
        return reverse('product-info', args=[self.slug])    



class Comment(models.Model):
    name = models.CharField(max_length=50)
    product = models.ForeignKey(Product, related_name='comments', on_delete=models.CASCADE)
    subject = models.CharField(max_length=50, blank=True)
    comment = models.TextField(max_length=150, blank=True)
    rate = models.IntegerField(default=1)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
        
        class CommentForm(models.Model):
            class Meta:
                model = Comment
                fields = ['subject', 'comment', 'rate']



