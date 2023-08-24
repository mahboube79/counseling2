from django.shortcuts import render
from .forms import Exam1,exam2,exam3,exam4,exam5,exam6,exam7,exam8



def all_exam(request):
    return render(request,"exam_app/all_exam.html")
    
    
    
    
def exam1(request):
    context={}
    if request.method=="POST":
        form=Exam1(request.POST)
        if form.is_valide():
            data=form.cleaned_data
        
        else:
            context["error_message"]="form is not valide ..."
            
    else:
        form=Exam1
    context["form"]=form    
    
    return render(request,"exam_app/show_exam.html",context)
    
    
    
    
    
    # # if form.is_valide():
    #     # data=form.cleane_data
        
    # context={'form':form}    
    # return render(request,"exam_app/show_exam.html",context)

















def exam2(request):
    return render(request,"exam_app/show_exam.html")
def exam3(request):
    return render(request,"exam_app/show_exam.html")
def exam4(request):
    return render(request,"exam_app/show_exam.html")
def exam5(request):
    return render(request,"exam_app/show_exam.html")
def exam6(request):
    return render(request,"exam_app/show_exam.html")
def exam7(request):
    return render(request,"exam_app/show_exam.html")
def exam8(request):
    return render(request,"exam_app/show_exam.html")
