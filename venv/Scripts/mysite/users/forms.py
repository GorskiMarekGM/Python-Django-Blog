from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

# whenever model validates it will create new user
# keeps the configuration in one place
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

#create form to update user model
#inherites from forms.ModelForm
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username','email']

#create form to update profile model
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields=['image']