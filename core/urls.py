from django.urls import path 
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('chains', views.chains, name = 'chains'),
    path('admin', views.admin, name = 'admin'),
    path('cart', views.cart, name = 'cart'),
    path('profile', views.profile, name = 'profile'),
]