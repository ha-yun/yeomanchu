import csv

from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.hashers import make_password
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.

from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import CreateView, DetailView

from accountapp.forms import YMTISIGN
from accountapp.models import YMTI



class YdateLogin(LoginView):

    def get_success_url(self):
        return reverse('accountapp:detail',kwargs={'pk':self.request.user.pk})


class AccountCreateView(CreateView):
    model = YMTI
    form_class = YMTISIGN
    success_url = reverse_lazy('articleapp:list')
    template_name = 'create.html'


def blogin(request):
    return render(request, 'blogin.html')

class AccountDetailView(DetailView):
    model = YMTI
    context_object_name = 'target_user'
    template_name = 'detail.html'


## ymti회원 데이터를 YMTI 모델에 추가
# with open('static/ymti_edit_data00.csv',newline='') as csvfile:
#     data_reader = csv.DictReader(csvfile)
#     for row in data_reader:
#         YMTI.objects.create(
#         username=row['mem_id'],
#         password= make_password(row['mem_no']),
#         mem_sex = row['mem_sex'],
#         mem_age = row['mem_age'],
#         mem_loc = row['mem_loc'],
#         mem_birth_ddi = row['mem_birth_ddi'],
#         mate_blood = row['mate_blood'],
#         pf_ins_yn = row['pf_ins_yn'],
#         mbti_code = row['mbti_code'],
#         food_cat =row['food_cat'],
#         concn =row['concn'],
#         )
