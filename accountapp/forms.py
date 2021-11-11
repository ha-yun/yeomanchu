from django import forms
from django.contrib.auth.forms import UserCreationForm

from accountapp.models import YMTI
from django.contrib.auth.forms import AuthenticationForm

class YMTISIGN(UserCreationForm):
  class Meta:
    model = YMTI
    fields = ['username','password']

# class YdateLoginform(AuthenticationForm):
#   class Meta:
#     model = YMTI
#     fields = ['username','password']

