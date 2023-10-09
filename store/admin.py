from django.contrib import admin

from .models import Category, Product

@admin.register(Category)
class adminCategory(admin.ModelAdmin):
    list_display = ['name']
    list_filter = ['name']
    search_fields = ['name']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Product)
class adminProduct(admin.ModelAdmin):
    list_display = ['created_by', 'title', 'slug', 'price','in_stock']
    list_filter = ['title', 'price', 'in_stock', 'category']
    list_editable = ['price']
    search_fields = ['title', 'category', 'created_by']
    prepopulated_fields = {'slug': ('title',)}



    






 