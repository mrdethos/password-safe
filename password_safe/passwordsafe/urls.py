from django.contrib import admin
from django.urls import path, include
from base import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('loginpage/', views.login_request, name='loginpage'),
    path('signup/', views.register_request, name='signup'),
    path('logout/', views.logout_request, name='logout'),
    path('password_list/', views.password_list, name='password_list'),
]
