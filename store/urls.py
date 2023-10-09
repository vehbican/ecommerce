from django.urls import path
from .views import all_categories,category_products,product_detail



urlpatterns = [
    path('', all_categories, name='all_categories'),
    path('category/<slug:category_slug>/', category_products, name='category_products'),
    path('product/<str:product_slug>/', product_detail, name='product_detail')
]

app_name = 'store'