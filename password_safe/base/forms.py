from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Submit, MultiField, Div, Field

class NewUserForm(UserCreationForm):
    username    = forms.CharField(
        label='Username', 
        widget=forms.TextInput(attrs={"class": "form-control mb-3", 'placeholder': 'Your Name'})
        )
    email       = forms.EmailField(
        label='Email', 
        max_length=50, 
        widget=forms.EmailInput(attrs={"class":"form-control  mb-3",'placeholder': 'user@email.com'})
        )
    password1   = forms.CharField(
        label='Password', 
        widget=forms.PasswordInput(attrs={"class":"form-control mb-3"})
        )
    password2   = forms.CharField(
        label='Password confirmation',
        widget=forms.PasswordInput(attrs={"class":"form-control mb-3"})
        )
    class Meta:
        model  = User
        fields = ("username", "email", "password1", "password2")
        
    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
