import csv

from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.

from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import CreateView, DetailView

from accountapp.forms import YMTISIGN
from accountapp.models import YMTI



# class YdateLogin(LoginView):
#
#     def get_success_url(self):
#         return reverse('accountapp:detail',kwargs={'pk':self.request.user.pk})

# def YdateLogin(request):
#     form = YdateLoginform(request.POST or None)
#     if request.method=="POST" and form.is_valid():
#         username = form.cleaned_data['username']
#         password = form.cleaned_data['password']
#         user = authenticate(request,username=username, password=password)
#         if user is not None:
#             login(request, user=user)
#             ydata = YMTI.objects.get(username=password)
#             return HttpResponseRedirect(reverse('accountapp:detail',kwargs={'pk':ydata.id}))
#         else:
#             error = " Sorry! Username and Password didn't match, Please try again ! "
#     return render(request, 'login.html', {'form': form})
#

def YdateLogin(request):
    if request.method != 'POST':
        form = AuthenticationForm()
    else:
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('accountapp:detail',kwargs={'pk':user.id}))
            else:
                print('user not found')
    return render(request, 'login.html', {'form':form})


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


## ydate_user 데이터 추가
# with open('static/ymti_edit_data00.csv',newline='') as csvfile:
#     data_reader = csv.DictReader(csvfile)
#     for row in data_reader:
#         YMTI.objects.create(
#         username=row['mem_id'],
#         password= row['mem_no'],
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


