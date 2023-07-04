from django.db import models
from django.contrib.auth.models import User as U
from django.contrib.auth.models import AbstractUser

# Create your models here.


class PayPlan(models.Model):
    name = models.CharField(max_length=20)
    price = models.IntegerField()
    updated_at = models.DateTimeField(auto_now=True)
    create_at = models.DateTimeField(auto_now_add=True)

# # 장고가 생성하는 유저모델은 슈퍼유저등을 관리
# # 장고 유저모델을 상속받는다고 하지만 엄연히 다르다.
# # User로 일대일 매칭을 해줘야 shortner 유저를 바라보는 것.

class Users(AbstractUser):
    pay_plan = models.ForeignKey(PayPlan, on_delete=models.DO_NOTHING)

class UserDetail(models.Model):
    user = models.OneToOneField(Users, on_delete=models.CASCADE)
    pay_plan = models.ForeignKey(PayPlan, on_delete=models.DO_NOTHING)