from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib import messages

# Create your views here.

def reg_form(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Wellcome {'username'}!')
            return redirect('products_store-index')
    else:
        form = UserRegisterForm()

    return render(request, 'customers/register.html', {'form':form})

