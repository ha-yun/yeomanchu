from django.urls import path

from articleapp.views import ydate, YONE, YTHREE, YTWO, RECOMMEND

app_name = 'articleapp'

urlpatterns = [
    path('list/', ydate, name='list'),
    path('recommend/<int:pk>',RECOMMEND.as_view(), name='recommend'),
    path('yone/<int:pk>', YONE.as_view(), name='yone'),
    path('ytwo/<int:pk>', YTWO.as_view(), name='ytwo'),
    path('ythree/<int:pk>', YTHREE.as_view(), name='ythree'),
    ]