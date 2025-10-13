from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='products_store-index'),
    path('tools/', views.tools, name='products_store-tools'),
    path('contact/', views.contact, name='products_store-contact'),
    path('', views.index, name='products_store-delivery_page'),
    path('', views.index, name='products_store-register_page'),
    path('', views.index, name='products_store-login_page'),
    path('', views.index, name='products_store-basket_page'),
    path('', views.index, name='products_store-logout'),
]
