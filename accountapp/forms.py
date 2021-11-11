from django import forms
from django.contrib.auth.forms import UserCreationForm

from accountapp.models import YMTI


class YMTISIGN(UserCreationForm):
  class Meta:
    model = YMTI
    fields = ['username','password']


# class YdateLoginform(forms.Form):
#   username=forms.CharField()
#   password=forms.CharField(widget=forms.PasswordInput())

