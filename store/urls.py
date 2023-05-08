from django.urls import path
from . import views

urlpatterns = [
    path('', views.store, name='store'),
    # Dinamic links for each product
    path('product/<slug:slug>/', views.product_info, name='product-info'),
      # Dinamic links for each category
    path('search/<slug:category_slug>/', views.category_list, name='category-list'),
]