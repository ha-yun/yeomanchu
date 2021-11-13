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

    # 첫 번째 추천(음식)
    def food(self):
        user = self.request.user
        mem_id = user.mem_no    # mem_id = 1379275
        food = find_food_person(mem_id, 1)['mbti_code']
        return food
    # 두 번째 추천(로그기반)
    def log(self):
        user = self.request.user
        mem_id = user.mem_no
        log = find_log(mem_id,1)['mbti_code']
        return log
    # 세 번째 추천(YMTI)
    def ymti_recommend(self):
        user = self.request.user
        mem_id = user.mem_no
        df_ymti = find_ymti(mem_id,30)
        df_ymti = df_ymti.sort_values(by='concn', axis=0,ascending=False)
        ymti_recommend = df_ymti[:1]['mbti_code']
        return ymti_recommend

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






