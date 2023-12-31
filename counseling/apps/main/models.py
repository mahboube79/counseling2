from django.db import models
from django.utils import timezone
from apps.accounts.models import CustomUser
from django.urls import reverse


# Create your models here.

class Blog(models.Model):
    blog_title=models.CharField(max_length=200,verbose_name="عنوان مقاله")
    blog_summery=models.TextField(max_length=500,verbose_name="خلاصه مقاله")
    blog_text= models.TextField(verbose_name="متن مقاله")
    main_img=models.ImageField(upload_to='images/blogimg/',verbose_name="تصویر",default=None)
    register_date=models.DateTimeField(default=timezone.now)
    is_active=models.BooleanField(default=False)
    user_registered=models.ForeignKey(CustomUser, on_delete=models.CASCADE,null=True)
    
    # def get_absolute_url(self):
    #     return reverse('article_detail',args=[str(self.id)])
    
#-----------------------------------------------------------------------------
class Videos(models.Model):
    title=models.CharField(max_length=200,verbose_name="عنوان ویدئو")
    video=models.FileField(upload_to='video/videos/',verbose_name="ویدئو")
    poster=models.ImageField(upload_to='images/videoposter/',verbose_name="پوستر ویدئو",default=None)
    register_date=models.DateTimeField(default=timezone.now)
    is_active=models.BooleanField(default=False)
    user_registered=models.ForeignKey(CustomUser, on_delete=models.CASCADE,null=True)
    
    
    
    
    
    
#-----------------------------------------------------------------------------
class Consultant(models.Model):
    name=models.CharField(max_length=100)
    education=models.CharField(max_length=200)
    resume=models.CharField(max_length=500)
    img=models.ImageField(upload_to='images/counselimg/')
    