from django.shortcuts import render , redirect
from .forms import *
from .models import ResultExam
from django.contrib.auth.decorators import login_required
import matplotlib.pyplot as plt
from io import BytesIO
import base64
from django.conf import settings

dic={
    'ress1':'',
    'ress2':'',
    'ress3':'',
    'ress4':'',
    'ress5':'',
    'ress6':'',
    'ress7':'',
    'ress8':'',    
}

def media_admin(request):
    return {'media_url':settings.MEDIA_URL,}

def all_exam(request):
    return render(request,"exam_app/all_exam.html",{'media_url':settings.MEDIA_URL})
    
# ----------------------------------------------------------------------------------
@login_required
def firstexam(request):
    return render(request,"exam_app/exam1.html",{'media_url':settings.MEDIA_URL})
# ----------------------------------------------------------------------------------

def exam1(request):
    context={}
    if request.method == "POST":
        form=Exam1(request.POST)
        n=1
        sum=0
        for item in form:
            q=int(request.POST[f'q{n}'])
            n+=1
            sum+=q
            
        dic['ress1']=sum
        return redirect('exam:exam2')
    else:
        form=Exam1
    context={
        'form':form,
        'lable':'آزمون اول',
        'titr':'استعداد زبانی',
    }   
    return render(request,"exam_app/show_exam.html",context)


def exam2(request):
    context={}
    if request.method == "POST":
        form=Exam2(request.POST)
        n=1
        sum=0
        for item in form:
            q=int(request.POST[f'q{n}'])
            n+=1
            sum+=q
        dic['ress2']=sum
        return redirect('exam:exam3')
    else:
        form=Exam2
    context={
        'form':form,
        'lable':'آزمون دوم:',
        'titr':'استعداد منطقی - ریاضی'
    }     
    return render(request,"exam_app/show_exam.html",context)


def exam3(request):
    context={}
    if request.method == "POST":
        form=Exam3(request.POST)
        n=1
        sum=0
        for item in form:
            q=int(request.POST[f'q{n}'])
            n+=1
            sum+=q
        dic['ress3']=sum
        return redirect('exam:exam4')
    else:
        form=Exam3
    context={
        'form':form,
        'lable':'آزمون سوم:',
        'titr':'استعداد فضائی'
    }     
    return render(request,"exam_app/show_exam.html",context)


def exam4(request):
    context={}
    if request.method == "POST":
        form=Exam4(request.POST)
        n=1
        sum=0
        for item in form:
            q=int(request.POST[f'q{n}'])
            n+=1
            sum+=q
        dic['ress4']=sum
        return redirect('exam:exam5')
    else:
        form=Exam4
    context={
        'form':form,
        'lable':'آزمون چهارم:',
        'titr':'استعداد بدنی - جنبشی'
    }     
    return render(request,"exam_app/show_exam.html",context)


def exam5(request):
    context={}
    if request.method == "POST":
        form=Exam5(request.POST)
        n=1
        sum=0
        for item in form:
            q=int(request.POST[f'q{n}'])
            n+=1
            sum+=q
        dic['ress5']=sum
        return redirect('exam:exam6')
    else:
        form=Exam5
    context={
        'form':form,
        'lable':'آزمون پنجم',
        'titr':'استعداد موسیقی'
    }     
    return render(request,"exam_app/show_exam.html",context)


def exam6(request):
    context={}
    if request.method == "POST":
        form=Exam6(request.POST)
        n=1
        sum=0
        for item in form:
            q=int(request.POST[f'q{n}'])
            n+=1
            sum+=q
        dic['ress6']=sum
        return redirect('exam:exam7')
    else:
        form=Exam6
    context={
        'form':form,
        'lable':'آزمون ششم:',
        'titr':'استعداد طبیعت گرا'
    }     
    return render(request,"exam_app/show_exam.html",context)


def exam7(request):
    context={}
    if request.method == "POST":
        form=Exam7(request.POST)
        n=1
        sum=0
        for item in form:
            q=int(request.POST[f'q{n}'])
            n+=1
            sum+=q
        dic['ress7']=sum
        return redirect('exam:exam8')
    else:
        form=Exam7
    context={
        'form':form,
        'lable':'آزمون هفتم',
        'titr':'استعداد بین فردی'
    }     
    return render(request,"exam_app/show_exam.html",context)


def exam8(request):
    context={}
    if request.method == "POST":
        form=Exam8(request.POST)
        n=1
        sum=0
        for item in form:
            q=int(request.POST[f'q{n}'])
            n+=1
            sum+=q
        dic['ress8']=sum    
        return redirect('exam:showResult')
    else:
        form=Exam8
    context={
        'form':form,
        'lable':'آزمون هشتم:',
        'titr':' استعداد برون فردی'
    }     
    return render(request,"exam_app/show_exam.html",context)

# ----------------------------------------------------------------------------------  
def showResult(request):
    resultexam=ResultExam()
    resultexam.name=request.user.name
    resultexam.family=request.user.family
    resultexam.user_registered=request.user.mobile_number
    resultexam.ress1=dic['ress1']
    resultexam.ress2=dic['ress2']
    resultexam.ress3=dic['ress3']
    resultexam.ress4=dic['ress4']
    resultexam.ress5=dic['ress5']
    resultexam.ress6=dic['ress6']
    resultexam.ress7=dic['ress7']
    resultexam.ress8=dic['ress8']
    resultexam.save()
    context={
        'res':resultexam
    }
    return redirect('exam:ressChart')

# ----------------------------------------------------------------------------------  
def ressChart(request):
    finallyress=ResultExam.objects.all()
    counts=[]
    for item in finallyress:
        if item.name==request.user.name and item.family==request.user.family:
            counts.append(item.ress1)
            counts.append(item.ress2)
            counts.append(item.ress3)
            counts.append(item.ress4)
            counts.append(item.ress5)
            counts.append(item.ress6)
            counts.append(item.ress7)
            counts.append(item.ress8)
    lable=['زبانی','منطقی-ریاضی','فضائی','بدنی-جنبشی','موسیقی','طبیعت گرا','بین فردی','درون فردی']
    plt.rcParams['font.family'] = 'B yekan'
    plt.pie(counts, labels=lable, autopct='%1.1f%%')
    plt.title('')
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8').replace('\n', '')
    # plt.show()

    return render(request,"exam_app/result.html",{'image': image_base64}) 

# ----------------------------------------------------------------------------------
@login_required
def secondexam(request):
    return render(request,"exam_app/exam2.html",{'media_url':settings.MEDIA_URL})
# ----------------------------------------------------------------------------------
def autism(request):
    context={}
    if request.method == "POST":
        form=Autism(request.POST)
        n=1
        sum=0
        for item in form:
            q=int(request.POST[f'q{n}'])
            n+=1
            sum+=q
        ress=sum
        return render(request,"exam_app/result2.html",{'ress':ress})
    else:
        form=Autism
    context={
        'form':form,
        'lable':'آزمون رفتار های تکراری',
        'titr':' '
    }     
    return render(request,"exam_app/show_exam.html",context)