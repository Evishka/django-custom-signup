from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ('first_name','last_name', 'email','personal_url')
    
    def signup(self, request, user):
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.personal_url = self.cleaned_data['personal_url']
        user.save()

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('first_name','last_name', 'email','personal_url')