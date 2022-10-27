from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class NewUserForm(UserCreationForm):
    username    = forms.CharField(
        label='', 
        widget=forms.TextInput(attrs={"class": "form-control mb-3", 'placeholder': 'Your Name'})
        )
    email       = forms.EmailField(
        required=True,
        label='', 
        max_length=50, 
        widget=forms.EmailInput(attrs={"class":"form-control  mb-3",'placeholder': 'user@email.com'})
        )
    password1   = forms.CharField(
        label='', 
        widget=forms.PasswordInput(attrs={"class":"form-control mb-3", 'placeholder': 'Your password'})
        )
    password2   = forms.CharField(
        label='',
        widget=forms.PasswordInput(attrs={"class":"form-control mb-3", 'placeholder': 'Password confirmation'})
        )
    class Meta:
        model  = User
        fields = ("username", "email", "password1", "password2")
        
    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=True)
        user.username = self.cleaned_data['username']
        user.email = self.cleaned_data['email']
        user.password1 = self.cleaned_data['password1']
        user.password2 = self.cleaned_data['password2']

        
        if commit:
            user.save()
        return user
