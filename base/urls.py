from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('products', views.products, name='products'),
    path('blogs', views.blog, name='blog'),
    path('blog/<slug:slug>', views.blog_detail, name='blog_detail'),
    path('product/<slug:slug>', views.product_detail, name='product_detail'),
    path('contact', views.contact, name='contact'),
]