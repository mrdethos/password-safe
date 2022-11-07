from django.contrib import admin
from django.urls import path
from base import views
from base.views import PasswordCreate, PasswordUpdate, PasswordDelete

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('loginpage/', views.login_request, name='loginpage'),
    path('signup/', views.register_request, name='signup'),
    path('logout/', views.logout_request, name='logout'),
    path('password_list/', views.password_list, name='password_list'),
    path('password-create/', PasswordCreate.as_view(), name='password-create'),
    path('password-update/<int:pk>/', PasswordUpdate.as_view(), name='password-update'),
    path('password-delete/<int:pk>/', PasswordDelete.as_view(), name='password-delete'),
]
