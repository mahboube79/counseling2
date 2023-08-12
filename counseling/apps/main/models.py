from django.db import models
from django.utils import timezone
from apps.accounts.models import CustomUser

# Create your models here.

class Blog(models.Model):
    blog_title=models.CharField(max_length=200,verbose_name="عنوان مقاله")
    blog_text= models.TextField(verbose_name="متن")
    register_date=models.DateTimeField(default=timezone.now)
    is_active=models.BooleanField(default=False)
    user_registered=models.ForeignKey(CustomUser, on_delete=models.CASCADE,null=True)
    
    def __str__(self):
        return self.blog_title
#-----------------------------------------------------------------------------
def upload_gallery_image(instance,filename):
    return f"images/blog/gallery/{filename}"

class BlogGallery(models.Model):
    blog_image_name=models.ImageField(upload_to=upload_gallery_image,verbose_name="تصویر")
    blog=models.ForeignKey(Blog,on_delete=models.CASCADE,null=True,related_name='images')


#------------------------------------------------------------------------------    
class Like(models.Model):
    user_liked=models.ForeignKey(CustomUser,on_delete=models.CASCADE,null=True)
    blog=models.ForeignKey(Blog,on_delete=models.CASCADE,null=True)

#-----------------------------------------------------------------------------
