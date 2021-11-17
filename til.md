# Ydate
[211021]
- startapp accountapp
- base.html(head,header,footer.html)
- startapp articleapp

[211022]
- accountapp/templates/create, login.html url and views
- articleapp/templates/list.html url and views
- static/base.css
- pip install django-bootstrap4

[211027]
- login and create(AccountCreateView, AccountDetailView, blogin)
- create jewerly fields : YMTI(AbstractUser)model -- custom(Django User)
    - migrate

[211028]
- accountapp/templates/detail.html
- templates/header.html
    - {% if user.is_authenticated %}

[211029]
- link google font
- accountapp/templates/detail.html
    - {% if user == target_user %}

[211101]
- articleapp/templates/recommend.html
- articleapp/templates/yone, ytwo, ythree.html
    - articleapp/views.py

[211102]
- https://developers.kakao.com/sdk/js/kakao.js
    - kakao link 

[211103]
- share link (facebook, twitter, kakao)

[211104]
- share link image (facebook, twitter, kakao)

[211105]
- class loginview(LoginView): def get_success_url

[211108]
- login and y_recommend css

[211110]
- YDATA model 만들고 회원 데이터 db에 추가
  - views.py에 ydate_user 데이터 추가
    ```
     with open('static/ymti_edit_data00.csv',newline='') as csvfile:
         data_reader = csv.DictReader(csvfile)
         for row in data_reader:
             YMTI.objects.create(
             username=row['mem_id'],
             password= row['mem_no'],
             mem_sex = row['mem_sex'],
             mem_age = row['mem_age'],
             mem_loc = row['mem_loc'],
             mem_birth_ddi = row['mem_birth_ddi'],
             mate_blood = row['mate_blood'],
             pf_ins_yn = row['pf_ins_yn'],
             mbti_code = row['mbti_code'],
             food_cat =row['food_cat'],
             concn =row['concn'],
             )
        ```
- YdataLogin 수정즁, db에 넣은 회원 데이터로 로그인이 안됨!

[211111]
- AuthenticationForm, authenticate() 적용 x

[211112]
- yuser데이터를 db에 넣을 때 해시화해서 넣기
  - password= make_password(row['mem_no'])
  - 비밀번호 암호화 관련 참고링크 : https://docs.djangoproject.com/en/3.2/topics/auth/passwords/#django.contrib.auth.hashers.PBKDF2PasswordHasher
- accountapp/templates/detail.html 
  - 로그인한 회원 mbti_code에 따라 보석이름 보여주기

[211113]
- Recommendation_System 파일의 모델과 연결
  - 회원 추천(food, log, ymti)
  
[211114]
- dating_course 파일의 모델과 연결
  - 데이트 코스 추천(place, food)
  - 장소 링크
- create.html 수정

[211115]
- star.html 파일 추가(별똥별 효과)
  - html,json,css
- Cafe24Oneprettynight font 추가
- detail.html 보석 이미지 추가
- blogin.html에 card button 추가

[211116]
- decorator : yuser(func)
  - @method_decorator(yuser, name='dispatch')
- blogin.html에 ios-15 구슬 효과 추가
- home page 수정

[211117]

