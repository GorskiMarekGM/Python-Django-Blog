from django.shortcuts import render, redirect
from django.contrib import messages
#messages.debug
#messages.info
#messages.success
#messages.warning
#messages.error

#our own user registration to replace usercreation form
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required


# Create views
def register(request):
    # if post is active create request with POST data
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            #flash message - popping just once
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
    # blank form for none post request
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form':form})

#user must be logged in to access this page 
@login_required
#Create profile
def profile(request):
    #when form is submited, and takes new data
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        #if both of them are correct data can be sent
        if u_form.is_valid() and p_form.is_valid():
            #saving both profiles
            u_form.save()
            p_form.save()

            messages.success(request, f'Your account has been updated!')
            return redirect('profile')
    
    else:
    #for not submited form with past data
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    #passing to template
    context = {
        'u_form':u_form,
        'p_form':p_form
    }
    return render(request, 'users/profile.html', context)