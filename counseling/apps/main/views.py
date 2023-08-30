from multiprocessing import context
from django.shortcuts import render,redirect
from django.views import View
from django.conf import settings
from django.contrib.auth.decorators import login_required
from .models import Blog
from .forms import BlogForm
from django.core.files.storage import FileSystemStorage
import os 
import datetime
from django.conf import settings


def media_admin(request):
    return {'media_url':settings.MEDIA_URL,}

#-------------------------------------------------------------
class MainView(View):
    def get(self,request,*args,**kwargs):
        blogs=Blog.objects.all()
        list_blog=Blog.objects.order_by('register_date').reverse()[:4]
        return render(request,"main_app/index.html",{'list_blog':list_blog})
    
#-------------------------------------------------------------
def showblog(request):
    blogs=Blog.objects.all()
    context={
        "blogs":blogs,
        'media_url':settings.MEDIA_URL,
    }
    return render(request,"main_app/showblog.html",context)

#-------------------------------------------------------------------------
@login_required
def create_blog(request):
    if request.method=="POST":
        form = BlogForm(request.POST,request.FILES)
        if form.is_valid():
            imageUpload = request.FILES['main_img']
            imgName , ext = os.path.splitext(imageUpload.name)
            currenttime = datetime.datetime.utcnow().strftime("%Y%m%d%H%M%S%f")
            imagePath = 'images/blogimg/'+imgName+currenttime+ext
            data=form.cleaned_data
            blog=Blog()
            blog.blog_title=data['blog_title']
            blog.blog_text=data['blog_text']
            blog.blog_summery=data['blog_summery']
            blog.main_img=imagePath
            
            blog.save()
            fss=FileSystemStorage()
            fss.save(imagePath,imageUpload)            
            return render(request,"main_app/index.html")
    else:
        form=BlogForm()
        context={
            'form':form
        }
        return render(request,'main_app/register_blog.html',context)
