from django.shortcuts import render, redirect
from .forms import UserRegisterForm, UserUpdateDetailsForm, User_profileUpdateForm
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
    if request.method == 'POST':
        uud_form = UserUpdateDetailsForm(request.POST, instance=request.user)
        upu_form = User_profileUpdateForm(request.POST, request.FILES, instance=request.user.user_profile)

        if uud_form.is_valid() and upu_form.is_valid():
            uud_form.save()
            upu_form.save()
            messages.success(request, f'User details successfuly updated!')
            return redirect('customers-profile_page')
    else:
        uud_form = UserUpdateDetailsForm(instance=request.user)
        upu_form = User_profileUpdateForm(instance=request.user.user_profile)



    content = {
        'uud_form': uud_form,
        'upu_form': upu_form
    }
    return render(request, 'customers/profile.html', content)

