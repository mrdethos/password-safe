from django.shortcuts import render, redirect
from .forms import NewUserForm
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import StoredPassword


def home(request):
    if request.user.is_authenticated:
        return redirect('password_list/')
    return render(request, 'base/home.html')

def loginpage(request):
    return render(request, 'base/loginpage.html')

def signup(request):
    return render(request, 'base/signup.html')

def register_request(request):
    if request.user.is_authenticated:
        return redirect('../password_list/')
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("home")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render(request=request, template_name="base/signup.html", context={"register_form":form})

def login_request(request):
    if request.user.is_authenticated:
        return redirect('../password_list/')
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"Welcome, {username}.")
                return redirect("home")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="base/loginpage.html", context={"login_form":form})

def logout_request(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect("home")

def password_list(request):
    password = StoredPassword.objects.filter(user=request.user)
    context = {'passwords': password}
    return render(request, 'base/password_list.html', context)

class PasswordCreate(LoginRequiredMixin, CreateView):
    model  = StoredPassword
    fields = ['title', 'description', 'password']
    success_url = reverse_lazy('password_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(PasswordCreate, self).form_valid(form)

class PasswordUpdate(LoginRequiredMixin, UpdateView):
    model = StoredPassword
    fields = ['title', 'description', 'password']
    success_url = reverse_lazy('password_list')

class PasswordDelete(LoginRequiredMixin, DeleteView):
    model = StoredPassword
    context_object_name = 'password'
    success_url = reverse_lazy('password_list')
