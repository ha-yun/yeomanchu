from django.contrib.auth.views import LogoutView
from django.urls import path

from accountapp.views import blogin, AccountDetailView, AccountCreateView, YdateLogin

app_name = 'accountapp'

urlpatterns = [
    path('login/', YdateLogin, name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('create/', AccountCreateView.as_view(), name='create'),
    path('detail/<int:pk>', AccountDetailView.as_view(), name='detail'),
    path('blogin/', blogin, name='blogin'),
]