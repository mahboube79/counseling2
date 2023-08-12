from multiprocessing import context
from django.shortcuts import render,redirect
from django.views import View
from django.conf import settings
from django.forms import modelformset_factory
from .models import BlogGallery,Blog
from .forms import BlogGalleryForm ,BlogForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required



def media_admin(request):
    return {'media_url':settings.MEDIA_URL,}

#-------------------------------------------------------------
class MainView(View):
    def get(self,request,*args,**kwargs):
        blogs=Blog.objects.all()
        return render(request,"main_app/index.html",{"blogs":blogs})
    
#-------------------------------------------------------------
@login_required
def add_blog(request):
    ImageFormSet=modelformset_factory(BlogGallery,form=BlogGalleryForm)
    if request.method=='GET':
        blog_form=BlogForm()
        image_formset=ImageFormSet(queryset=BlogGallery.objects.none(),)
        context={
            "blog_form":blog_form,
            "image_formset":image_formset
        }
        return render(request,"main_app/register_blog.html",context)
    
    
    
    elif request.method=="POST":
        blog_form=BlogForm(request.POST)
        image_formsset=ImageFormSet(request.POST,request.FILES)
        if blog_form.is_valid() and image_formsset.is_valid():
            blog_obj=blog_form.save()
            
            for form in image_formsset.cleaned_data:
                if form:
                    BlogGallery.objects.create(
                        blog_image_name=form['blog_image_name'],
                        blog=blog_obj
                    )
            messages.success(request,'ثبت مقاله با موفقیت انجام شد','success')       
            return redirect('main:index')
        else:
            return render(request,"main_app/register_blog.html",{"blog_form":blog_form})