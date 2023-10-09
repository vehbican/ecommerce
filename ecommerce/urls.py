"""
URL configuration for ecommerce project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path
from store import views
from store.views import all_categories, category_products, product_detail
from django.contrib.auth import views as auth_views
from accounts import urls as accounts_urls, views as accounts_views  
from basket import views as basketViews #add_to_basket, remove_from_basket, view_basket


urlpatterns = [
    path('admin/', admin.site.urls),
    path('category/<slug:category_slug>/', category_products, name='category_products'),
    path('product/<slug:product_slug>/', product_detail, name='product_detail'),
    path('', include(accounts_urls)),  
    path('', include('store.urls', namespace='store')),
    path('add_to_basket/<int:product_id>/', basketViews.add_to_basket, name='add_to_basket'),
    path('remove_from_basket/<int:product_id>/', basketViews.remove_from_basket, name='remove_from_basket'),
    path('basket/', basketViews.view_basket, name='basket_view'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
