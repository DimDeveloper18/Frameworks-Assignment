"""
URL configuration for tools_store project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path, include
from customers import views as customers_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('products_store.urls')),
    path('', include('custom_comments.urls')),
    path('register/', customers_views.reg_form, name='customers-reg_form'),
    path('login/', auth_views.LoginView.as_view(template_name='customers/login.html'), name='customers-login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='customers/logout.html'), name='customers-logout'),
    path('basket/', customers_views.basket_page, name='customers-basket_page'),
    path('profile/', customers_views.profile_page, name='customers-profile_page'),
]
