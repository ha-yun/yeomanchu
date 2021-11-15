import os
import pandas as pd
import numpy as np
import itertools
import warnings  
warnings.filterwarnings('ignore')

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# 데이터 불러오기
path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'static/data/profile_ymti_data_ver2')
path2 = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'static/data/log_data_1027_2')
df = pd.read_csv(path+'\ymti_data.csv',engine='c',encoding='UTF-8')                                     # 원데이터
df_2030 = pd.read_csv(path + '\ymti_edit_data.csv',engine='c',encoding='UTF-8')                         # 20,30대 YMTI 데이터

want_df = pd.read_csv(path2 + '\want_log.csv',engine='c',encoding='UTF-8')                              # 만나고 싶어요 로그
concn_df = pd.read_csv(path2 + '\concn_log.csv',engine='c',encoding='UTF-8')                            # 관심있어요 로그
msg_df = pd.read_csv(path2 + '\msg_log.csv',engine='c',encoding='UTF-8')                                # 메세지 로그
pf_view_df = pd.read_csv(path2 + '\pf_view_log.csv',engine='c',encoding='UTF-8')                        # 프로필 열람 로그

married_df = pd.read_csv(path2 + '\married_success_sample.csv',engine='c',encoding='UTF-8')             # 결혼 성공 사례 로그

## 1. 음식 카테로리별 추천===============================================================================================
# 데이터 변환 전부 완료된 상태에서 진행('음식카테고리 분류' 및 '문자열 객체로 변환'이 완료된 상태)

# 피처 벡터 행렬 변환
count_vect = CountVectorizer(min_df=0, ngram_range=(1, 2))
food_mat = count_vect.fit_transform( df_2030['food_cat']  )
# 코사인 유사도 계산
food_sim = cosine_similarity(food_mat, food_mat)
# 유사도가 높은 순으로 정리된 food_sim_sorted_ind 객체의 비교 행 위치 인덱스 값
food_sim_sorted_ind = food_sim.argsort()[:, ::-1]

def find_food_cat(df, sorted_ind, mem_id):
    title_mem = df_2030[ df_2030['mem_no'] == mem_id] 
    title_index = title_mem.index.values
    sim_indexs = sorted_ind[ title_index]

    sim_indexs = sim_indexs.reshape(-1)
    return df.iloc[sim_indexs]
      
def find_food_person(mem_id,top_n):
    a = df_2030[ df_2030['mem_no'] == mem_id]
    if a.mem_sex.values =="f":
        return find_food_cat(df_2030, food_sim_sorted_ind, mem_id )[find_food_cat(df_2030, food_sim_sorted_ind, mem_id )['mem_sex']=="m"][:top_n]
    elif a.mem_sex.values =="m":
        return find_food_cat(df_2030, food_sim_sorted_ind, mem_id )[find_food_cat(df_2030, food_sim_sorted_ind, mem_id )['mem_sex']=="f"][:top_n]
    

## 2. 로그 선호도별 추천===============================================================================================
# 4개의 로그데이터 결과 INFP와 ISFP가 압도적으로 높게 산출됨
prefer = df_2030[(df_2030['mbti_code']=='INFP')| (df_2030['mbti_code']=='ISFP')]

def find_log(mem_id,top_n):
    a = df_2030[df_2030['mem_no'] == mem_id]
    if a.mem_sex.values =="f":
        df_shuffled = prefer[prefer['mem_sex']=="m"].sample(frac=1)
        return(df_shuffled[:top_n])
        
    elif a.mem_sex.values =="m":
        df_shuffled = prefer[prefer['mem_sex']=="f"].sample(frac=1)
        return(df_shuffled[:top_n])


## 3. YMTI 기반 1:1 추천===============================================================================================
# '만나고 싶어요' 로그 있을 시 상단에 추천목록에 먼저 뜰 수 있도록 함

# 만나고 싶어요 데이터 셋 가져오기
concn_df['concn']=int(1)
concn_df = concn_df[['mem_no','concn']]
# 2030기반 데이터에 숫자 삽입
df_2030['concn']=int(0)
# 로그데이터와 2030 데이터 교집합 찾기
df_inner = pd.merge(df_2030,concn_df,on='mem_no',suffixes=("_df2030", ""))
df_inner = df_inner.drop(['concn_df2030'],axis=1)
# 중복제거
df_inner = df_inner.drop_duplicates()
# '만나고 싶어요' 데이터를 2030 데이터에 대입
df_2030['concn'] += df_inner['concn'] 
# 결측지 0으로 지정
df_2030 = df_2030.fillna(int(0))
    
def find_ymti(mem_id,top_n):
    a = df_2030[df_2030['mem_no'] == mem_id]
    if a.mem_sex.values =="f":
        # 여자 일 때 - 남자 추천
        if a.mbti_code.values=="ISTJ":
            b = df_2030[df_2030['mem_sex']=="m"]
            c = b[b['mbti_code']=="ESTP"].sample(frac=1)
            return(c[:top_n])
        elif a.mbti_code.values=="ISFJ":
            b = df_2030[df_2030['mem_sex']=="m"]
            c = b[b['mbti_code']=="ESFP"].sample(frac=1)
            return(c[:top_n])
        elif a.mbti_code.values=="INFJ":
            b = df_2030[df_2030['mem_sex']=="m"]
            c = b[b['mbti_code']=="ENFP"].sample(frac=1)
            return(c[:top_n])
        elif a.mbti_code.values=="INTJ":
            b = df_2030[df_2030['mem_sex']=="m"]
            c = b[b['mbti_code']=="ENTP"].sample(frac=1)
            return(c[:top_n])
        elif a.mbti_code.values=="ISTP":
            b = df_2030[df_2030['mem_sex']=="m"]
            c = b[b['mbti_code']=="ESTJ"].sample(frac=1)
            return(c[:top_n])
        elif a.mbti_code.values=="ISFP":
            b = df_2030[df_2030['mem_sex']=="m"]
            c = b[b['mbti_code']=="ESFJ"].sample(frac=1)
            return(c[:top_n])
        elif a.mbti_code.values=="INFP":
            b = df_2030[df_2030['mem_sex']=="m"]
            c = b[b['mbti_code']=="ENFJ"].sample(frac=1)
            return(c[:top_n])
        elif a.mbti_code.values=="INTP":
            b = df_2030[df_2030['mem_sex']=="m"]
            c = b[b['mbti_code']=="ENTJ"].sample(frac=1)
            return(c[:top_n])
        elif a.mbti_code.values=="ESTP":
            b = df_2030[df_2030['mem_sex']=="m"]
            c = b[b['mbti_code']=="ISTJ"].sample(frac=1)
            return(c[:top_n])
        elif a.mbti_code.values=="ESFP":
            b = df_2030[df_2030['mem_sex']=="m"]
            c = b[b['mbti_code']=="ISFJ"].sample(frac=1)
            return(c[:top_n])
        elif a.mbti_code.values=="ENFP":
            b = df_2030[df_2030['mem_sex']=="m"]
            c = b[b['mbti_code']=="INFJ"].sample(frac=1)
            return(c[:top_n])
        elif a.mbti_code.values=="ENTP":
            b = df_2030[df_2030['mem_sex']=="m"]
            c = b[b['mbti_code']=="INTJ"].sample(frac=1)
            return(c[:top_n])
        elif a.mbti_code.values=="ESTJ":
            b = df_2030[df_2030['mem_sex']=="m"]
            c = b[b['mbti_code']=="ISTP"].sample(frac=1)
            return(c[:top_n])
        elif a.mbti_code.values=="ESFJ":
            b = df_2030[df_2030['mem_sex']=="m"]
            c = b[b['mbti_code']=="ISFP"].sample(frac=1)
            return(c[:top_n])
        elif a.mbti_code.values=="ENFJ":
            b = df_2030[df_2030['mem_sex']=="m"]
            c = b[b['mbti_code']=="INFP"].sample(frac=1)
            return(c[:top_n])
        elif a.mbti_code.values=="ENTJ":
            b = df_2030[df_2030['mem_sex']=="m"]
            c = b[b['mbti_code']=="INTP"].sample(frac=1)
            return(c[:top_n])
           
    elif a.mem_sex.values =="m":
        # 남자 일 때 - 여자 추천
        if a.mbti_code.values=="ISTJ":
            b = df_2030[df_2030['mem_sex']=="f"]
            c = b[b['mbti_code']=="ESTP"].sample(frac=1)
            return(c[:top_n])
        elif a.mbti_code.values=="ISFJ":
            b = df_2030[df_2030['mem_sex']=="f"]
            c = b[b['mbti_code']=="ESFP"].sample(frac=1)
            return(c[:top_n])
        elif a.mbti_code.values=="INFJ":
            b = df_2030[df_2030['mem_sex']=="f"]
            c = b[b['mbti_code']=="ENFP"].sample(frac=1)
            return(c[:top_n])
        elif a.mbti_code.values=="INTJ":
            b = df_2030[df_2030['mem_sex']=="f"]
            c = b[b['mbti_code']=="ENTP"].sample(frac=1)
            return(c[:top_n])
        elif a.mbti_code.values=="ISTP":
            b = df_2030[df_2030['mem_sex']=="f"]
            c = b[b['mbti_code']=="ESTJ"].sample(frac=1)
            return(c[:top_n])
        elif a.mbti_code.values=="ISFP":
            b = df_2030[df_2030['mem_sex']=="f"]
            c = b[b['mbti_code']=="ESFJ"].sample(frac=1)
            return(c[:top_n])
        elif a.mbti_code.values=="INFP":
            b = df_2030[df_2030['mem_sex']=="f"]
            c = b[b['mbti_code']=="ENFJ"].sample(frac=1)
            return(c[:top_n])
        elif a.mbti_code.values=="INTP":
            b = df_2030[df_2030['mem_sex']=="f"]
            c = b[b['mbti_code']=="ENTJ"].sample(frac=1)
            return(c[:top_n])
        elif a.mbti_code.values=="ESTP":
            b = df_2030[df_2030['mem_sex']=="f"]
            c = b[b['mbti_code']=="ISTJ"].sample(frac=1)
            return(c[:top_n])
        elif a.mbti_code.values=="ESFP":
            b = df_2030[df_2030['mem_sex']=="f"]
            c = b[b['mbti_code']=="ISFJ"].sample(frac=1)
            return(c[:top_n])
        elif a.mbti_code.values=="ENFP":
            b = df_2030[df_2030['mem_sex']=="f"]
            c = b[b['mbti_code']=="INFJ"].sample(frac=1)
            return(c[:top_n])
        elif a.mbti_code.values=="ENTP":
            b = df_2030[df_2030['mem_sex']=="f"]
            c = b[b['mbti_code']=="INTJ"].sample(frac=1)
            return(c[:top_n])
        elif a.mbti_code.values=="ESTJ":
            b = df_2030[df_2030['mem_sex']=="f"]
            c = b[b['mbti_code']=="ISTP"].sample(frac=1)
            return(c[:top_n])
        elif a.mbti_code.values=="ESFJ":
            b = df_2030[df_2030['mem_sex']=="f"]
            c = b[b['mbti_code']=="ISFP"].sample(frac=1)
            return(c[:top_n])
        elif a.mbti_code.values=="ENFJ":
            b = df_2030[df_2030['mem_sex']=="f"]
            c = b[b['mbti_code']=="INFP"].sample(frac=1)
            return(c[:top_n])
        elif a.mbti_code.values=="ENTJ":
            b = df_2030[df_2030['mem_sex']=="f"]
            c = b[b['mbti_code']=="INTP"].sample(frac=1)
            return(c[:top_n])
    
mem_id =30302

# # sim_food = find_food_cat(df_2030, food_sim_sorted_ind, mem_id )
# print("=="*60)
# print("본인 : \n",df_2030[df_2030['mem_no']== mem_id])
# print("=="*60)
# print("첫 번째 추천(음식) : \n",find_food_person(mem_id,1))
# print("두 번째 추천(로그기반) : \n",find_log(mem_id,1))

df_ymti = find_ymti(mem_id,30)
df_ymti = df_ymti.sort_values(by='concn', axis=0,ascending=False)
# print("세 번째 추천(YMTI) : \n",df_ymti[:1])