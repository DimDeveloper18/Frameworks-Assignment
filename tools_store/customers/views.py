from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

def reg_form(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Registration completed {'username'}! Please login.')
            return redirect('customers-login')
    else:
        form = UserRegisterForm()

    return render(request, 'customers/register.html', {'form':form})

@login_required
def basket_page(request):
    return render(request, 'customers/basket.html')

@login_required
def profile_page(request):
    return render(request, 'customers/profile.html')

