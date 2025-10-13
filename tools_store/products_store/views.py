from django.shortcuts import render
from django.http import HttpResponse




# Create your views here.
def index(request):
    return render(request, 'products_store/index.html')

def tools(request):
    return render(request, 'products_store/tools.html')

def contact(request):
    return render(request, 'products_store/contact.html')
