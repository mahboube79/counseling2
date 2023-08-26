from django import forms

CHICES_EXAM=[
        ("1","هرگز"),
        ("2","گاهی"),
        ("3","اغلب"),
        ("4","همیشه")
    ]

class Exam1(forms.Form):
    # هوش زبانی
    q1=forms.ChoiceField(label="وانمود به کتاب خواندن می کند و به داستان ها گوش می دهد.",
                         widget=forms.RadioSelect(attrs={'class':'form-check-inline ch'}),choices=CHICES_EXAM)
    q2=forms.ChoiceField(label="از گفتگوها و بحث ها لذت می برد.",
                            widget=forms.RadioSelect(attrs={'class':'form-check-inline ch'}),choices=CHICES_EXAM)
    q3=forms.ChoiceField(label="بازی های حفظی را دوست دارد",
                            widget=forms.RadioSelect(attrs={'class':'form-check-inline ch'}),choices=CHICES_EXAM)
    q4=forms.ChoiceField(label="از جملات قافیه دار،معماگونه و سرکار گذاشتن دیگران لذت می برد.",
                            widget=forms.RadioSelect(attrs={'class':'form-check-inline ch'}),choices=CHICES_EXAM)
    


class Exam2(forms.Form):
    # هوش منطقی ریاضی
    
    q1=forms.ChoiceField(label="سوال می پرسد.",
                            widget=forms.RadioSelect(attrs={'class':'form-check-inline ch'}),choices=CHICES_EXAM)
    q2=forms.ChoiceField(label="از بررسی چیزها و شکل دادن به آن ها لذت می برد.",
                            widget=forms.RadioSelect(attrs={'class':'form-check-inline ch'}),choices=CHICES_EXAM)
    q3=forms.ChoiceField(label="الگو ها را بررسی و اکتشاف می کند.",
                            widget=forms.RadioSelect(attrs={'class':'form-check-inline ch'}),choices=CHICES_EXAM)
    q4=forms.ChoiceField(label="از حل کردن مسائل لذت می برد.",
                            widget=forms.RadioSelect(attrs={'class':'form-check-inline ch'}),choices=CHICES_EXAM)
    q5=forms.ChoiceField(label="از بازی روی تخته و مقوا لذت می برد.",
                            widget=forms.RadioSelect(attrs={'class':'form-check-inline ch'}),choices=CHICES_EXAM)
    q6=forms.ChoiceField(label="شمارش و گفتن اعداد را دوست دارد",
                            widget=forms.RadioSelect(attrs={'class':'form-check-inline ch'}),choices=CHICES_EXAM)
    
    

class Exam3(forms.Form):
# هوش فضایی
    q1=forms.ChoiceField(label="از کنار هم قرار دادن چیز ها و یا جدا کردن قطعات از همدیگرلذت می برد.",
                          widget=forms.RadioSelect(attrs={'class':'form-check-inline ch'}),choices=CHICES_EXAM)
    q2=forms.ChoiceField(label="از نقاشی و طراحی لذت می برد.",
                          widget=forms.RadioSelect(attrs={'class':'form-check-inline ch'}),choices=CHICES_EXAM)
    q3=forms.ChoiceField(label="از وصل کردن قطعات پازل لذت می برد.",
                            widget=forms.RadioSelect(attrs={'class':'form-check-inline ch'}),choices=CHICES_EXAM)
    q4=forms.ChoiceField(label="چیز های جدید خلق می کند",
                            widget=forms.RadioSelect(attrs={'class':'form-check-inline ch'}),choices=CHICES_EXAM)
    q5=forms.ChoiceField(label="رویا پردازی می کند",
                            widget=forms.RadioSelect(attrs={'class':'form-check-inline ch'}),choices=CHICES_EXAM)
    q6=forms.ChoiceField(label="از تماشای تصاویر و فیلم ها لذت می برد.",
                            widget=forms.RadioSelect(attrs={'class':'form-check-inline ch'}),choices=CHICES_EXAM)
    
class Exam4(forms.Form):
    # هوش بدنی - جنبشی
    q1=forms.ChoiceField(label="از فعالیت جسمی لذت می برد.",
                            widget=forms.RadioSelect(attrs={'class':'form-check-inline ch'}),choices=CHICES_EXAM)
    q2=forms.ChoiceField(label=" حرکات موزون را دوست دارد.",
                            widget=forms.RadioSelect(attrs={'class':'form-check-inline ch'}),choices=CHICES_EXAM)
    q3=forms.ChoiceField(label="در اطراف اتاق حر کت می کند.",
                            widget=forms.RadioSelect(attrs={'class':'form-check-inline ch'}),choices=CHICES_EXAM)
    q4=forms.ChoiceField(label="از زبان بدن (حرکات دست و سر و..) استفاده می کند.",
                            widget=forms.RadioSelect(attrs={'class':'form-check-inline ch'}),choices=CHICES_EXAM)
    q5=forms.ChoiceField(label="اشیاء را لمس و بررسی می کند.",
                            widget=forms.RadioSelect(attrs={'class':'form-check-inline ch'}),choices=CHICES_EXAM)
    q6=forms.ChoiceField(label="از نقش بازی کردن لذت می برد.",
                            widget=forms.RadioSelect(attrs={'class':'form-check-inline ch'}),choices=CHICES_EXAM)
    q7=forms.ChoiceField(label="تجربیان لمسی (مثل بازی با ماسه ،نقاشی) را دوست دارد.",
                            widget=forms.RadioSelect(attrs={'class':'form-check-inline ch'}),choices=CHICES_EXAM)
    

class Exam5(forms.Form):
     # موسیقی
    q1=forms.ChoiceField(label="از آواز خواندن لذت می برد.",
                            widget=forms.RadioSelect(attrs={'class':'form-check-inline ch'}),choices=CHICES_EXAM)
    q2=forms.ChoiceField(label="ریتم آهنگ ها را به یاد دارد",
                            widget=forms.RadioSelect(attrs={'class':'form-check-inline ch'}),choices=CHICES_EXAM)
    q3=forms.ChoiceField(label="از بازی با ابزار آلات موسیقی لذت می برد.",
                            widget=forms.RadioSelect(attrs={'class':'form-check-inline ch'}),choices=CHICES_EXAM)
    q4=forms.ChoiceField(label="به موسیقی گوش می دهد.",
                            widget=forms.RadioSelect(attrs={'class':'form-check-inline ch'}),choices=CHICES_EXAM)
    q5=forms.ChoiceField(label="خودش آهنگ می سازد(با وسایل تولید کننده صدا)",
                            widget=forms.RadioSelect(attrs={'class':'form-check-inline ch'}),choices=CHICES_EXAM)
    q6=forms.ChoiceField(label="با شنیدن موسقی واکنش نشان می دهد.",
                            widget=forms.RadioSelect(attrs={'class':'form-check-inline ch'}),choices=CHICES_EXAM)
    q7=forms.ChoiceField(label="زمزمه می کند و سوت می زند.",
                            widget=forms.RadioSelect(attrs={'class':'form-check-inline ch'}),choices=CHICES_EXAM)
    


class Exam6(forms.Form):
   # طبیعت گرا
    q1=forms.ChoiceField(label="در مورد حیوانات اهلی حرف می زند.",
                            widget=forms.RadioSelect(attrs={'class':'form-check-inline ch'}),choices=CHICES_EXAM)
    q2=forms.ChoiceField(label="دوست دارد گیاهان و حیوانات اهلی را به کلاس بیاورد.",
                            widget=forms.RadioSelect(attrs={'class':'form-check-inline ch'}),choices=CHICES_EXAM)
    q3=forms.ChoiceField(label="کلکسیونی از حشرات  و سنگ ها و چیز های دیگر طبیعی دارد.",
                            widget=forms.RadioSelect(attrs={'class':'form-check-inline ch'}),choices=CHICES_EXAM)
    q4=forms.ChoiceField(label="به مشاهده پرندگان، پروانه ها و ابرها می پردازد.",
                            widget=forms.RadioSelect(attrs={'class':'form-check-inline ch'}),choices=CHICES_EXAM)
    q5=forms.ChoiceField(label="چیز های موجود در طبیعت را به کلاس می برد.",
                            widget=forms.RadioSelect(attrs={'class':'form-check-inline ch'}),choices=CHICES_EXAM)
    q6=forms.ChoiceField(label="از تجربیات بیرون از خانه و مدرسه و سفر لذت می برد.",
                            widget=forms.RadioSelect(attrs={'class':'form-check-inline ch'}),choices=CHICES_EXAM)
    

class Exam7(forms.Form):
    
    # بین فردی
    q1=forms.ChoiceField(label="از بازی با دوستانش لذت می برد.",
                            widget=forms.RadioSelect(attrs={'class':'form-check-inline ch'}),choices=CHICES_EXAM)
    q2=forms.ChoiceField(label="با دیگران گفتگو می کند.",
                            widget=forms.RadioSelect(attrs={'class':'form-check-inline ch'}),choices=CHICES_EXAM)
    q3=forms.ChoiceField(label="دوستان زیادی دارد.",
                            widget=forms.RadioSelect(attrs={'class':'form-check-inline ch'}),choices=CHICES_EXAM)
    q4=forms.ChoiceField(label="ویژگی های رهبری را نشان می دهد.",
                            widget=forms.RadioSelect(attrs={'class':'form-check-inline ch'}),choices=CHICES_EXAM)
    q5=forms.ChoiceField(label="فعالیت ها را سازماندهی می کند.",
                            widget=forms.RadioSelect(attrs={'class':'form-check-inline ch'}),choices=CHICES_EXAM)
    q6=forms.ChoiceField(label="از فعالیت های گروهی لذت می برد.",
                            widget=forms.RadioSelect(attrs={'class':'form-check-inline ch'}),choices=CHICES_EXAM)
    q7=forms.ChoiceField(label="دوست دارد به دیگران کمک کند.",
                            widget=forms.RadioSelect(attrs={'class':'form-check-inline ch'}),choices=CHICES_EXAM)



class Exam8(forms.Form):
  # درون فردی
    q1=forms.ChoiceField(label="از تنها کار کردن لذت می برد.",
                            widget=forms.RadioSelect(attrs={'class':'form-check-inline ch'}),choices=CHICES_EXAM)
    q2=forms.ChoiceField(label="به دنبال ارضای غرایزش است.",
                            widget=forms.RadioSelect(attrs={'class':'form-check-inline ch'}),choices=CHICES_EXAM)
    q3=forms.ChoiceField(label="علایقش را دنبال می کند.",
                            widget=forms.RadioSelect(attrs={'class':'form-check-inline ch'}),choices=CHICES_EXAM)
    q4=forms.ChoiceField(label="از فکر کردن و تامل نمودن لذت می برد.",
                            widget=forms.RadioSelect(attrs={'class':'form-check-inline ch'}),choices=CHICES_EXAM)
    q5=forms.ChoiceField(label="دوست دارد برای خودش فضای شخصی داشته باشد.",
                            widget=forms.RadioSelect(attrs={'class':'form-check-inline ch'}),choices=CHICES_EXAM)
    q6=forms.ChoiceField(label="بیشتر از کارهای گروهی، کارهای انفرادی را دوست دارد.",
                            widget=forms.RadioSelect(attrs={'class':'form-check-inline ch'}),choices=CHICES_EXAM)
    q7=forms.ChoiceField(label="دوست دارد خودش کارهایش را انجام دهد.",
                            widget=forms.RadioSelect(attrs={'class':'form-check-inline ch'}),choices=CHICES_EXAM)