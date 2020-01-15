from django.contrib.auth.views import LogoutView
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

from .forms import AuthenticationForm

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(form_class=AuthenticationForm,
                                                template_name='accounts/login.html'),
        name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', views.profile, name='profile'),
]
