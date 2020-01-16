from django import forms
from django.contrib.auth.forms import AuthenticationForm as BaseAuthenticationForm
from django.contrib.auth.forms import PasswordResetForm as BasePasswordResetForm
from django.contrib.auth.forms import SetPasswordForm as BaseSetPasswordForm
from django.contrib.auth.forms import UsernameField
from django.contrib.auth import password_validation
from django.utils.translation import gettext, gettext_lazy as _


class AuthenticationForm(BaseAuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={
        'autofocus': True,
        'class': 'form-control',
        'placeholder': _('Enter username')
    }))
    password = forms.CharField(label=_("Password"), strip=False,
                               widget=forms.PasswordInput(attrs={
                                   'autocomplete': 'current-password',
                                   'class': 'form-control'
                               }))


class PasswordResetForm(BasePasswordResetForm):
    email = forms.EmailField(
        label=_("Email"),
        max_length=254,
        widget=forms.EmailInput(attrs={'autocomplete': 'email', 'class': 'form-control', 'autofocus': True})
    )


class SetPasswordForm(BaseSetPasswordForm):
    new_password1 = forms.CharField(
        label=_("New password"),
        widget=forms.PasswordInput(attrs={'autocomplete': 'off', 'class': 'form-control', 'autofocus': True}),
        strip=False,
        help_text=password_validation.password_validators_help_text_html(),
    )
    new_password2 = forms.CharField(
        label=_("New password confirmation"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'off', 'class': 'form-control'}),
    )


class PasswordChangeForm(SetPasswordForm):
    old_password = forms.CharField(
        label=_("Old password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'current-password', 'autofocus': True, 'class': 'form-control'}),
    )