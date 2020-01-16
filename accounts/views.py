from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils.translation import gettext, gettext_lazy as _


@login_required
def profile(request):
    return render(request, 'accounts/profile.html', {'title': _('Profile'), 'pretitle': _('Manage your profile')})
