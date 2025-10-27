from django.shortcuts import render
from django.http import HttpResponse
from .models import Comment


# Create your views here.


def comments_view(request):
    com_consist = {
        'comments': Comment.objects.all()
    }
    return render(request, 'custom_comments/comments_page.html', com_consist)

