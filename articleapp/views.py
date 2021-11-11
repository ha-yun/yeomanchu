from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.views.generic import DetailView

from accountapp.models import YMTI


def ydate(request):
    return render(request,'list.html')

class RECOMMEND(DetailView):
    model = YMTI
    context_object_name = 'target'
    template_name = 'recommend.html'


class YONE(DetailView):
    model = YMTI
    context_object_name = 'target_yone'
    template_name = 'yone.html'

class YTWO(DetailView):
    model = YMTI
    context_object_name = 'target_ytwo'
    template_name = 'ytwo.html'

class YTHREE(DetailView):
    model = YMTI
    context_object_name = 'target_ythree'
    template_name = 'ythree.html'
