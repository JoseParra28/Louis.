from django.urls import path
from . import views

urlpatterns = [
    path('', views.store, name='store'),
    path('cart/', views.cart, name="cart"),
	path('checkout/', views.checkout, name="checkout"),
    path('update_item/', views.updateItem, name="update_item"),
    path('product/<slug:slug>/', views.product_info, name='product-info'),
    path('search/<slug:category_slug>/', views.category_list, name='category-list'),
    path('add-review', views.add_review, name='add-review'),
]