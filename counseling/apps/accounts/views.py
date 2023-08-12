from typing import Any
from django import http
from django.shortcuts import render, redirect
from django.views import View
from .forms import RegisterUserForm,LoginUserForm
from .models import CustomUser
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

class RegisterUserView(View):
    def dispatch(self,request,*args,**kwargs):
        if request.user.is_authenticated :
            return redirect('main:index')
        return super().dispatch(request,*args,**kwargs)
    
    def get(self,request,*args,**kwargs):
        form=RegisterUserForm()
        return render(request,"accounts_app/register.html",{"form":form})
    
    
    def post(self,request, *args , **kwargs):
        form=RegisterUserForm(request.POST)
        if form.is_valid():
            user=form.cleaned_data
            CustomUser.objects.create_user(
                email=user['email'],
                name=user['name'],
                family=user['family'],
                mobile_number=user['mobile_number'],
                password=user['password']
            )
            messages.success(request,'ثبت نام با موفقیت انجام شد','success')
            return redirect('main:index')
        else:
            messages.error(request,'اطلاعات وارد شده معتبر نمی باشد','error')
            return render(request,"accounts_app/register.html",{"form":form})
# -----------------------------------------------------------------
class LoginUserView(View):
    def dispatch(self,request,*args,**kwargs):
        if request.user.is_authenticated :
            return redirect('main:index')
        return super().dispatch(request,*args,**kwargs)
    
    def get(self ,request, *args,**kwargs):
        form=LoginUserForm()
        return render(request,"accounts_app/login.html",{"form":form})
    
    def post(self, request,*args ,**kwargs):
        form=LoginUserForm(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            user=authenticate(username=cd.get('email'),password=cd.get('password'))
            if user is not None:
                db_user=CustomUser.objects.get(email=user.email)
                if not db_user.is_admin:
                    messages.success(request,'ورود با موقیت انجام شد')
                    login(request,user)
                    next_url=request.GET.get('next')
                    if next_url is not None:
                        return redirect(next_url)
             
                    else:
                        return redirect('main:index')
             
                else:
                    messages.warning(request,'کاربر ادمین نمی تواند از این صفحه وارد شود')
                    return render(request,"accounts_app/login.html",{"form":form})
          
            else:
                messages.warning(request,'نام کاربری یا رمز عبور اشتباه است')
                return render(request,"accounts_app/login.html",{"form":form})
                
        else:
            messages.warning(request,'اطلاعات وارد شده صحیح نمی باشد')
            return render(request,"accounts_app/login.html",{"form":form})
            
            
# -----------------------------------------------------------
class LogoutUserView(View):
    def dispatch(self,request,*args,**kwargs):
        if not request.user.is_authenticated :
            return redirect('main:index')
        return super().dispatch(request,*args,**kwargs)
    
    def get(self,request,*args,**kwargs):
        logout(request)
        messages.success(request,'خروج از سایت با موفقیت انجام شد')
        return redirect('main:index')
