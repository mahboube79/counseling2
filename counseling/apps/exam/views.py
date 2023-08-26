from django.shortcuts import render , redirect
from .forms import Exam1,Exam2,Exam3,Exam4,Exam5,Exam6,Exam7,Exam8
from .models import ResultExam
from django.contrib.auth.decorators import login_required

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

def all_exam(request):
    return render(request,"exam_app/all_exam.html")
    
  
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
        'dic':dic
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
        return render(request,"exam_app/all_exam.html",context)
    else:
        form=Exam8
    context={
        'form':form,
        'lable':'آزمون هشتم:',
        'titr':' استعداد برون فردی'
    }     
    return render(request,"exam_app/show_exam.html",context)



def showResult(request):
    resultexam=ResultExam()
    resultexam.name=request.user.name
    resultexam.family=request.user.family
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
        'resss':resultexam
    }
    return render(request,"exam_app/all_exam.html",context)