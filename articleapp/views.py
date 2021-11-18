from django.shortcuts import render

# Create your views here.
from django.utils.decorators import method_decorator
from django.views.generic import DetailView


from accountapp.models import YMTI

## 회원 추천을 위한 Recommendation_System파일 호출
from static.Recommendation_System2 import *
## 데이트코스 추천을 위한 dating_course.py파일 호출
from static.dating_course2 import *



def ydate(request):
    return render(request,'list.html')


class RECOMMEND(DetailView):
    model = YMTI
    context_object_name = 'target'
    template_name = 'recommend.html'

    # 첫 번째 추천(음식)
    def food(self):
        user = self.request.user
        mem_id = user.mem_no
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
        yone_place_list = []
        for i in yone_place_date:
            yone_place_list.append(i)
        return yone_place_list[0]
    def yone_place_date_link(self):
        user = self.request.user
        mem_id = user.mem_no
        yone_place_date = first_dating_course(mem_id,1)
        yone_place_list = []
        for i in yone_place_date:
            yone_place_list.append(i)
        return yone_place_list[1]

    def yone_food_date(self):
        user = self.request.user
        mem_id = user.mem_no
        yone_food_date = first_food_course(mem_id,1)
        yone_food_list = []
        for i in yone_food_date:
            yone_food_list.append(i)
        return yone_food_list[0]
    def yone_food_date_link(self):
        user = self.request.user
        mem_id = user.mem_no
        yone_food_date = first_food_course(mem_id,1)
        yone_food_list = []
        for i in yone_food_date:
            yone_food_list.append(i)
        return yone_food_list[1]



## 2. 두 번째 사람에 대한 장소, 음식점 추천(로그 기반 사람 추천)
class YTWO(DetailView):
    model = YMTI
    context_object_name = 'target_ytwo'
    template_name = 'ytwo.html'

    def ytwo_place_date(self):
        user = self.request.user
        mem_id = user.mem_no
        ytwo_place_date = second_dating_course(mem_id,1)
        ytwo_place_list = []
        for i in ytwo_place_date:
            ytwo_place_list.append(i)
        return ytwo_place_list[0]
    def ytwo_place_date_link(self):
        user = self.request.user
        mem_id = user.mem_no
        ytwo_place_date = second_dating_course(mem_id,1)
        ytwo_place_list = []
        for i in ytwo_place_date:
            ytwo_place_list.append(i)
        return ytwo_place_list[1]

    def ytwo_food_date(self):
        user = self.request.user
        mem_id = user.mem_no
        ytwo_food_date = second_food_course(mem_id,1)
        ytwo_food_list = []
        for i in ytwo_food_date:
            ytwo_food_list.append(i)
        return ytwo_food_list[0]
    def ytwo_food_date_link(self):
        user = self.request.user
        mem_id = user.mem_no
        ytwo_food_date = second_food_course(mem_id,1)
        ytwo_food_list = []
        for i in ytwo_food_date:
            ytwo_food_list.append(i)
        return ytwo_food_list[1]



## 3. 세 번째 사람에 대한 장소, 음식점 추천(YMTI 기반 사람 추천)
class YTHREE(DetailView):
    model = YMTI
    context_object_name = 'target_ythree'
    template_name = 'ythree.html'

    def ythree_place_date(self):
        user = self.request.user
        mem_id = user.mem_no
        ythree_place_date = third_dating_course(mem_id,1)
        ythree_place_list = []
        for i in ythree_place_date:
            ythree_place_list.append(i)
        return ythree_place_list[0]
    def ythree_place_date_link(self):
        user = self.request.user
        mem_id = user.mem_no
        ythree_place_date = third_dating_course(mem_id,1)
        ythree_place_list = []
        for i in ythree_place_date:
            ythree_place_list.append(i)
        return ythree_place_list[1]

    def ythree_food_date(self):
        user = self.request.user
        mem_id = user.mem_no
        ythree_food_date = third_food_course(mem_id,1)
        ythree_food_list = []
        for i in ythree_food_date:
            ythree_food_list.append(i)
        return ythree_food_list[0]
    def ythree_food_date_link(self):
        user = self.request.user
        mem_id = user.mem_no
        ythree_food_date = third_food_course(mem_id,1)
        ythree_food_list = []
        for i in ythree_food_date:
            ythree_food_list.append(i)
        return ythree_food_list[1]





