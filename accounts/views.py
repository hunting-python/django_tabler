from django.contrib.auth.decorators import login_required
from django.shortcuts import render


# Create your views here.
def login(request):
    return render(request, 'accounts/login.html')


@login_required
def profile(request):
    return render(request, 'accounts/profile.html', {'title': 'Profile'})
