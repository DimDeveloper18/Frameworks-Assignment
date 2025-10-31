from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm


# Create your views here.

def reg_form(request):
    form = UserCreationForm()
    return render(request, 'customers/register.html', {'form':form})

