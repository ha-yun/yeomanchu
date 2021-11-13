from django.shortcuts import render

# Create your views here.
from django.views.generic import DetailView


from accountapp.models import YMTI

#회원 추천을 위한 Recommendation_System파일 호출
from static.Recommendation_System import *

def ydate(request):
    return render(request,'list.html')

class RECOMMEND(DetailView):
    model = YMTI
    context_object_name = 'target'
    template_name = 'recommend.html'

    def food(self):
        # mem_id = YMTI.objects.order_by('mem_id')
        mem_id = 1379275
        food = find_food_person(mem_id, 1)['mbti_code']
        return food

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






