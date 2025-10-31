from django.urls import path
from . import views


urlpatterns = [
    path('reg_form/', views.customers_view, name='customers/reg_form-view'),
]