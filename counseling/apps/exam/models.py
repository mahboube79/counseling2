from django.db import models
from apps.accounts.models import CustomUser

class ResultExam(models.Model):
    user_registered=models.ForeignKey(CustomUser,on_delete=models.CASCADE,null=True)
    name=models.CharField(max_length=200)
    family=models.CharField(max_length=200)
    ress1=models.IntegerField()
    ress2=models.IntegerField()
    ress3=models.IntegerField()
    ress4=models.IntegerField()
    ress5=models.IntegerField()
    ress6=models.IntegerField()
    ress7=models.IntegerField()
    ress8=models.IntegerField()
    