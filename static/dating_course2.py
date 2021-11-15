from static.Recommendation_System2 import *
import random

###### 데이트 코스 데이터 정제
## 1. 내부/외부=========================================================================================================
df = pd.read_csv(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'static/data/date_data.csv'))

# 데이터 결측지 제거
df_inside = df[['inside']].dropna(axis=0).sample(frac=1)
df_outside = df[['outside']].dropna(axis=0).sample(frac=1)

inside=[df_inside.values[i].tolist()[0].split() for i in range(len(df_inside))]
outside=[df_outside.values[i].tolist()[0].split() for i in range(len(df_outside))]
    
# 데이터 분리
df_inside = pd.DataFrame(columns=['inside','url'],data=inside)      # 내부 데이트 코스
df_outside = pd.DataFrame(columns=['outside','url'],data=outside)   # 외부 데이트 코스

## 2.음식==============================================================================================================
df_food = df[['western', 'chinese', 'japanese', 'korean',
       'dessert', 'etc']].sample(frac=1)

western=[df_food['western'].values[i].split() for i in range(len(df_food))]
chinese=[df_food['chinese'].values[i].split() for i in range(len(df_food))]
japanese=[df_food['japanese'].values[i].split() for i in range(len(df_food))]
korean=[df_food['korean'].values[i].split() for i in range(len(df_food))]
dessert=[df_food['dessert'].values[i].split() for i in range(len(df_food))]   
etc=[df_food['etc'].values[i].split() for i in range(len(df_food))] 

# 데이터 분리
df_western = pd.DataFrame(columns=['western','url'],data=western)           # 양식
df_chinese = pd.DataFrame(columns=['chinese','url'],data=chinese)           # 중식
df_japanese = pd.DataFrame(columns=['japanese','url'],data=japanese)        # 일식
df_korean = pd.DataFrame(columns=['korean','url'],data=korean)              # 한식
df_dessert = pd.DataFrame(columns=['dessert','url'],data=dessert)           # 디저트
df_etc = pd.DataFrame(columns=['etc','url'],data=etc)                       # 기타(동남아, 멕시코 등)


###### 데이트 코스 추천
## 1. 첫 번째 사람에 대한 장소,음식점 추천(음식 기반 사람 추천)========================================================================================
def first_dating_course(mem_id,top_n):
    if (find_food_person(mem_id,top_n).mem_sex.values=="f") & (find_food_person(mem_id,top_n).mbti_code.values[0][0]=="E"):
        return df_outside['outside'][0], df_outside['url'][0]
    elif (find_food_person(mem_id,top_n).mem_sex.values=="f") & (find_food_person(mem_id,top_n).mbti_code.values[0][0]=="I"):
        return df_inside['inside'][0],df_inside['url'][0]
    elif (df_2030[df_2030['mem_no']==mem_id].mem_sex.values=="f") & (df_2030[df_2030['mem_no']==mem_id].mbti_code.values[0][0]=="E"):
        return df_outside['outside'][0],df_outside['url'][0]
    elif (df_2030[df_2030['mem_no']==mem_id].mem_sex.values=="f") & (df_2030[df_2030['mem_no']==mem_id].mbti_code.values[0][0]=="I"):
        return df_inside['inside'][0],df_inside['url'][0]
#'western', 'chinese', 'japanese', 'korean','dessert', 'etc'
def first_food_course(mem_id,top_n):
    if find_food_person(mem_id,top_n).food_cat.values[0].split()[0] =="western":
        return df_western['western'][0], df_western['url'][0]                                             
    elif find_food_person(mem_id,top_n).food_cat.values[0].split()[0] =="chinese":
        return df_chinese['chinese'][0], df_chinese['url'][0]
    elif find_food_person(mem_id,top_n).food_cat.values[0].split()[0] =="japanese":
        return df_japanese['japanese'][0], df_japanese['url'][0]
    elif find_food_person(mem_id,top_n).food_cat.values[0].split()[0] =="korean":
        return df_korean['korean'][0], df_korean['url'][0]
    elif find_food_person(mem_id,top_n).food_cat.values[0].split()[0] =="dessert":
        return df_dessert['dessert'][0], df_dessert['url'][0]
    else:
        return df_etc['etc'][0]

## 2. 두 번째 사람에 대한 장소, 음식점 추천(로그 기반 사람 추천)========================================================================================
def second_dating_course(mem_id,top_n):
    if (find_log(mem_id,top_n).mem_sex.values=="f") & (find_log(mem_id,top_n).mbti_code.values[0][0]=="E"):
        return df_outside['outside'][1], df_outside['url'][1]
    elif (find_log(mem_id,top_n).mem_sex.values=="f") & (find_log(mem_id,top_n).mbti_code.values[0][0]=="I"):
        return df_inside['inside'][1],df_inside['url'][1]
    elif (df_2030[df_2030['mem_no']==mem_id].mem_sex.values=="f") & (df_2030[df_2030['mem_no']==mem_id].mbti_code.values[0][0]=="E"):
        return df_outside['outside'][1],df_outside['url'][1]
    elif (df_2030[df_2030['mem_no']==mem_id].mem_sex.values=="f") & (df_2030[df_2030['mem_no']==mem_id].mbti_code.values[0][0]=="I"):
        return df_inside['inside'][1],df_inside['url'][1]
def second_food_course(mem_id,top_n):
    me = df_2030[df_2030['mem_no']==mem_id].food_cat.values[0].split()
    person = find_log(mem_id,top_n).food_cat.values[0].split()
    a = list(set(me).intersection(person))
    random.shuffle(a)
    if a[0] =="western":
        return df_western['western'][1], df_western['url'][1]                                             
    elif a[0] =="chinese":
        return df_chinese['chinese'][1], df_chinese['url'][1]
    elif a[0] =="japanese":
        return df_japanese['japanese'][1], df_japanese['url'][1]
    elif a[0] =="korean":
        return df_korean['korean'][1], df_korean['url'][1]
    elif a[0] =="dessert":
        return df_dessert['dessert'][1], df_dessert['url'][1]
    elif a[0] =="etc":
        return df_etc['etc'][1]
    elif len(a) == 0:
        return df_western['western'][1], df_western['url'][1]      

## 3. 세 번째 사람에 대한 장소, 음식점 추천(YMTI 기반 사람 추천)========================================================================================
def third_dating_course(mem_id,top_n):
    if (find_ymti(mem_id,top_n).mem_sex.values=="f") & (find_ymti(mem_id,top_n).mbti_code.values[0][0]=="E"):
            return df_outside['outside'][2], df_outside['url'][2]
    elif (find_ymti(mem_id,top_n).mem_sex.values=="f") & (find_ymti(mem_id,top_n).mbti_code.values[0][0]=="I"):
        return df_inside['inside'][2],df_inside['url'][2]
    elif (df_2030[df_2030['mem_no']==mem_id].mem_sex.values=="f") & (df_2030[df_2030['mem_no']==mem_id].mbti_code.values[0][0]=="E"):
        return df_outside['outside'][2],df_outside['url'][2]
    elif (df_2030[df_2030['mem_no']==mem_id].mem_sex.values=="f") & (df_2030[df_2030['mem_no']==mem_id].mbti_code.values[0][0]=="I"):
        return df_inside['inside'][2],df_inside['url'][2]
def third_food_course(mem_id,top_n):
    me = df_2030[df_2030['mem_no']==mem_id].food_cat.values[0].split()
    person = find_ymti(mem_id,top_n).food_cat.values[0].split()
    a = list(set(me).intersection(person))
    random.shuffle(a)
    if a[0] =="western":
        return df_western['western'][2], df_western['url'][2]                                             
    elif a[0] =="chinese":
        return df_chinese['chinese'][2], df_chinese['url'][2]
    elif a[0] =="japanese":
        return df_japanese['japanese'][2], df_japanese['url'][2]
    elif a[0] =="korean":
        return df_korean['korean'][2], df_korean['url'][2]
    elif a[0] =="dessert":
        return df_dessert['dessert'][2], df_dessert['url'][2]
    elif a[0] =="etc":
        return df_etc['etc'][2]
    elif len(a) == 0:
        return df_western['western'][2], df_western['url'][2]    



# mem_id = 1687672
#
# print("=="*62)
# print(" ★ 첫 번째 사람의 데이트 코스 추천 ★ ")
# print("데이트 장소 : ",first_dating_course(mem_id,1))
# print("음식점 : ", first_food_course(mem_id,1))
# print("=="*62)
# print(" ★ 두 번째 사람의 데이트 코스 추천 ★ ")
# print("데이트 장소 : ",second_dating_course(mem_id,1))
# print("음식점 : ", second_food_course(mem_id,1))
# print("=="*62)
# print(" ★ 세 번째 사람의 데이트 코스 추천 ★ ")
# print("데이트 장소 : ",third_dating_course(mem_id,1))
# print("음식점 : ", third_food_course(mem_id,1))
# print("=="*62)