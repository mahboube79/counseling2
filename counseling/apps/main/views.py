from multiprocessing import context
from django.shortcuts import render,redirect,get_object_or_404
from django.views import View
from django.conf import settings
from django.contrib.auth.decorators import login_required
from .models import Blog, Consultant,  Videos
from .forms import BlogForm,VideoForm
from django.core.files.storage import FileSystemStorage
import os 
import datetime
from django.conf import settings

#-------------------------------------------------------------------------
def media_admin(request):
    return {'media_url':settings.MEDIA_URL,}

#-------------------------------------------------------------
class MainView(View):
    def get(self,request,*args,**kwargs):
        blogs=Blog.objects.all()
        list_blog=Blog.objects.order_by('register_date').reverse()[:4]
        list_consultant=Consultant.objects.order_by('id').reverse()[:2]
        list_video=Videos.objects.order_by('id').reverse()[:4]
        context={
            'list_blog':list_blog,
            'list_consultant':list_consultant,
            'list_video':list_video
            }
        return render(request,"main_app/index.html",context)
    
#-------------------------------------------------------------
def showblog(request):
    blogs=Blog.objects.order_by('id').reverse()
    context={
        "blogs":blogs,
        'media_url':settings.MEDIA_URL,
    }
    return render(request,"main_app/showblog.html",context)
#-------------------------------------------------------------------------
def article_detail(request,article_id):
    article = get_object_or_404(Blog,blog_title=article_id)
    print(article)
    return render(request,"main_app/mainblog.html",{'article':article})
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

#-------------------------------------------------------------------------
@login_required
def create_video(request):
    if request.method=="POST":
        form = VideoForm(request.POST,request.FILES)
        if form.is_valid():
            imageUpload = request.FILES['poster']
            videoUpload= request.FILES['video']
            imgName , ext = os.path.splitext(imageUpload.name)
            videoName , root_ext = os.path.splitext(videoUpload.name)
            currenttime = datetime.datetime.utcnow().strftime("%Y%m%d%H%M%S%f")
            imagePath = 'images/videoposter/'+imgName+currenttime+ext
            videoPath = 'video/videos/'+videoName+currenttime+root_ext
            
            data=form.cleaned_data
            video=Videos()
            video.title=data['title']
            video.poster=imagePath
            video.video=videoPath

            video.save()
            fss=FileSystemStorage()
            fss.save(imagePath,imageUpload)
            fss.save(videoPath,videoUpload)          
            return render(request,"main_app/videos.html")
    else:
        form=VideoForm()
        context={
            'form':form
        }
        return render(request,'main_app/create_video.html',context)

#-------------------------------------------------------------------------
def videos(request):
    videos= Videos.objects.order_by('id').reverse()
    context={
        'videos':videos,
        'media_url':settings.MEDIA_URL
    }
    return render(request,"main_app/videos.html",context)
#-------------------------------------------------------------------------

def aboutus(request):
    return render(request,"main_app/aboutus.html",{'media_url':settings.MEDIA_URL})

#-------------------------------------------------------------------------
def consultant(request):
    consul=Consultant.objects.all()
    context={
        'consul':consul,
        'media_url':settings.MEDIA_URL,
    }
    return render(request,"main_app/consultant.html",context)