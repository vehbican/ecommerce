from django.db import models
from django.conf import settings




class Category(models.Model):
    name = models.CharField(max_length = 300, db_index = True)
    slug = models.SlugField(max_length = 300, unique = True)
    image = models.ImageField(upload_to = 'images/', default = 'category.jpeg')

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name
    

class Product(models.Model):
    category = models.ForeignKey(Category, related_name = 'product', on_delete = models.CASCADE)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE, related_name = 'product_owner')
    title = models.CharField(max_length = 300)
    description = models.TextField(blank = True)
    image = models.ImageField(upload_to = 'images/')
    slug = models.SlugField(max_length = 300)
    price = models.DecimalField(max_digits = 6, decimal_places = 2)
    in_stock = models.BooleanField(default = True)


    class Meta:
        verbose_name_plural = 'products'
        ordering = ('title',)


    def __str__(self):
        return self.title
    

    



    