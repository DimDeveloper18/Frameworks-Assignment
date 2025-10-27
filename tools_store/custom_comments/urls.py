from django.urls import path
from . import views


urlpatterns = [
    path('comments_view/', views.comments_view, name='custom_comments/comments-view'),
]
