from django.shortcuts import render

# Create your views here.
from django.views.generic import DetailView


from accountapp.models import YMTI

## 회원 추천을 위한 Recommendation_System파일 호출
from static.Recommendation_System import *
## 데이트코스 추천을 위한 dating_course.py파일 호출
from static.dating_course import *



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


## 1. 첫 번째 사람에 대한 장소,음식점 추천(음식 기반 사람 추천)
class YONE(DetailView):
    model = YMTI
    context_object_name = 'target_yone'
    template_name = 'yone.html'

    def yone_place_date(self):
        user = self.request.user
        mem_id = user.mem_no
        yone_place_date = first_dating_course(mem_id,1)
        return yone_place_date

    def yone_food_date(self):
        user = self.request.user
        mem_id = user.mem_no
        yone_food_date = first_food_course(mem_id,1)
        return yone_food_date


## 2. 두 번째 사람에 대한 장소, 음식점 추천(로그 기반 사람 추천)
class YTWO(DetailView):
    model = YMTI
    context_object_name = 'target_ytwo'
    template_name = 'ytwo.html'

    def ytwo_place_date(self):
        user = self.request.user
        mem_id = user.mem_no
        ytwo_place_date = second_dating_course(mem_id,1)
        return ytwo_place_date

    def ytwo_food_date(self):
        user = self.request.user
        mem_id = user.mem_no
        ytwo_food_date = second_food_course(mem_id,1)
        return ytwo_food_date



## 3. 세 번째 사람에 대한 장소, 음식점 추천(YMTI 기반 사람 추천)
class YTHREE(DetailView):
    model = YMTI
    context_object_name = 'target_ythree'
    template_name = 'ythree.html'

    def ythree_place_date(self):
        user = self.request.user
        mem_id = user.mem_no
        ythree_place_date = third_dating_course(mem_id,1)
        return ythree_place_date

    def ythree_food_date(self):
        user = self.request.user
        mem_id = user.mem_no
        ythree_food_date = third_food_course(mem_id,1)
        return ythree_food_date






