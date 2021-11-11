from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class YMTI(AbstractUser):
    mem_sex = models.TextField(null=True)
    mem_age = models.IntegerField(null=True)
    mem_loc = models.TextField(null=True)
    mem_birth_ddi = models.IntegerField(null=True)
    mate_blood = models.IntegerField(null=True)
    pf_ins_yn = models.TextField(null=True)
    mbti_code = models.TextField(null=True)
    food_cat = models.TextField(null=True)
    concn = models.FloatField(null=True)
