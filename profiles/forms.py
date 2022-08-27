from django import forms
from django.contrib.auth.models import User


class NewUserForm(forms.ModelForm):

    class Meta:
        model = User
        # fields = ['username', 'email', 'password1', 'password2']
        fields = '__all__'
