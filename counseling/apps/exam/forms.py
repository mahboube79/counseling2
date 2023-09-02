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
    
    q1=forms.ChoiceField(label="از بررسی چیزها و شکل دادن به آن ها لذت می برد.",
                            widget=forms.RadioSelect(attrs={'class':'form-check-inline ch'}),choices=CHICES_EXAM)
    q2=forms.ChoiceField(label="الگو ها را بررسی و اکتشاف می کند.",
                            widget=forms.RadioSelect(attrs={'class':'form-check-inline ch'}),choices=CHICES_EXAM)
    q3=forms.ChoiceField(label="از حل کردن مسائل لذت می برد.",
                            widget=forms.RadioSelect(attrs={'class':'form-check-inline ch'}),choices=CHICES_EXAM)
    q4=forms.ChoiceField(label="شمارش و گفتن اعداد را دوست دارد",
                            widget=forms.RadioSelect(attrs={'class':'form-check-inline ch'}),choices=CHICES_EXAM)
    
    
class Exam3(forms.Form):
# هوش فضایی
    q1=forms.ChoiceField(label="از نقاشی و طراحی لذت می برد.",
                          widget=forms.RadioSelect(attrs={'class':'form-check-inline ch'}),choices=CHICES_EXAM)
    q2=forms.ChoiceField(label="از وصل کردن قطعات پازل لذت می برد.",
                            widget=forms.RadioSelect(attrs={'class':'form-check-inline ch'}),choices=CHICES_EXAM)
    q3=forms.ChoiceField(label="چیز های جدید خلق می کند",
                            widget=forms.RadioSelect(attrs={'class':'form-check-inline ch'}),choices=CHICES_EXAM)
    q4=forms.ChoiceField(label="رویا پردازی می کند",
                            widget=forms.RadioSelect(attrs={'class':'form-check-inline ch'}),choices=CHICES_EXAM)

    
class Exam4(forms.Form):
    # هوش بدنی - جنبشی
    q1=forms.ChoiceField(label="از فعالیت جسمی لذت می برد.",
                            widget=forms.RadioSelect(attrs={'class':'form-check-inline ch'}),choices=CHICES_EXAM)
    q2=forms.ChoiceField(label=" حرکات موزون را دوست دارد.",
                            widget=forms.RadioSelect(attrs={'class':'form-check-inline ch'}),choices=CHICES_EXAM)
    q3=forms.ChoiceField(label="از زبان بدن (حرکات دست و سر و..) استفاده می کند.",
                            widget=forms.RadioSelect(attrs={'class':'form-check-inline ch'}),choices=CHICES_EXAM)
    q4=forms.ChoiceField(label="از نقش بازی کردن لذت می برد.",
                            widget=forms.RadioSelect(attrs={'class':'form-check-inline ch'}),choices=CHICES_EXAM)
    

class Exam5(forms.Form):
     # موسیقی
    q1=forms.ChoiceField(label="ریتم آهنگ ها را به یاد دارد",
                            widget=forms.RadioSelect(attrs={'class':'form-check-inline ch'}),choices=CHICES_EXAM)
    q2=forms.ChoiceField(label="به موسیقی گوش می دهد.",
                            widget=forms.RadioSelect(attrs={'class':'form-check-inline ch'}),choices=CHICES_EXAM)
    q3=forms.ChoiceField(label="خودش آهنگ می سازد(با وسایل تولید کننده صدا)",
                            widget=forms.RadioSelect(attrs={'class':'form-check-inline ch'}),choices=CHICES_EXAM)
    q4=forms.ChoiceField(label="با شنیدن موسقی واکنش نشان می دهد.",
                            widget=forms.RadioSelect(attrs={'class':'form-check-inline ch'}),choices=CHICES_EXAM)
    

class Exam6(forms.Form):
   # طبیعت گرا
    q1=forms.ChoiceField(label="در مورد حیوانات حرف می زند.",
                            widget=forms.RadioSelect(attrs={'class':'form-check-inline ch'}),choices=CHICES_EXAM)
    q2=forms.ChoiceField(label="کلکسیونی از حشرات  و سنگ ها و چیز های دیگر طبیعی دارد.",
                            widget=forms.RadioSelect(attrs={'class':'form-check-inline ch'}),choices=CHICES_EXAM)
    q3=forms.ChoiceField(label="به مشاهده پرندگان، پروانه ها و ابرها می پردازد.",
                            widget=forms.RadioSelect(attrs={'class':'form-check-inline ch'}),choices=CHICES_EXAM)
    q4=forms.ChoiceField(label="چیز های موجود در طبیعت را به کلاس می برد.",
                            widget=forms.RadioSelect(attrs={'class':'form-check-inline ch'}),choices=CHICES_EXAM)
    

class Exam7(forms.Form):  
    # بین فردی
    q1=forms.ChoiceField(label="دوستان زیادی داردواز بازی با دوستانش لذت می برد.",
                            widget=forms.RadioSelect(attrs={'class':'form-check-inline ch'}),choices=CHICES_EXAM)
    q2=forms.ChoiceField(label="با دیگران گفتگو می کند.",
                            widget=forms.RadioSelect(attrs={'class':'form-check-inline ch'}),choices=CHICES_EXAM)
    q3=forms.ChoiceField(label="ویژگی های رهبری را نشان می دهد.",
                            widget=forms.RadioSelect(attrs={'class':'form-check-inline ch'}),choices=CHICES_EXAM)
    q4=forms.ChoiceField(label="از فعالیت های گروهی لذت می برد.",
                            widget=forms.RadioSelect(attrs={'class':'form-check-inline ch'}),choices=CHICES_EXAM)


class Exam8(forms.Form):
  # درون فردی
    q1=forms.ChoiceField(label="علایقش را دنبال می کند.",
                            widget=forms.RadioSelect(attrs={'class':'form-check-inline ch'}),choices=CHICES_EXAM)
    q2=forms.ChoiceField(label="از فکر کردن و تامل نمودن لذت می برد.",
                            widget=forms.RadioSelect(attrs={'class':'form-check-inline ch'}),choices=CHICES_EXAM)
    q3=forms.ChoiceField(label="دوست دارد برای خودش فضای شخصی داشته باشد.",
                            widget=forms.RadioSelect(attrs={'class':'form-check-inline ch'}),choices=CHICES_EXAM)
    q4=forms.ChoiceField(label="بیشتر از کارهای گروهی، کارهای انفرادی را دوست دارد.",
                            widget=forms.RadioSelect(attrs={'class':'form-check-inline ch'}),choices=CHICES_EXAM)


# ----------------------------------------------------------------------------------
CHICES_EXAM2={
    ("1","هرگز یا به ندرت"),
    ("2","یک بار یا بیشتر در روز"),
    ("3","15بار یا بیشتر در روز"),
    ("4","30 بار یا بیشتر در روز")    
}

CHICES_EXAM3={
    ("1","هرگز یا به ندرت"),
    ("2","خفیف یا گاه به گاه"),
    ("3","آشکار یا قابل ملاحظه"),
    ("4","شدید یا حاد"),
    
}

class Autism(forms.Form):
    q1=forms.ChoiceField(label="دوست دارد اجسام را به صورت افقی یا با الگوی مشخصی مرتب کند؟",
                        widget=forms.RadioSelect(attrs={'class':'form-check-inline ch'}),choices=CHICES_EXAM2)

    q2=forms.ChoiceField(label="مکررا با اجسام ور می رود؟(مثلا دائما آنها را می چرخاند،یا با آن ها بازی می کند ، روی آنها ضربه می زند،آنها را می چرخاند)",
                        widget=forms.RadioSelect(attrs={'class':'form-check-inline ch'}),choices=CHICES_EXAM2)
    
    q3=forms.ChoiceField(label="پشت سر هم دور خودش می چرخد؟",
                        widget=forms.RadioSelect(attrs={'class':'form-check-inline ch'}),choices=CHICES_EXAM2)

    q4=forms.ChoiceField(label="موقع نشستن یا ایستاده، رو به جلو و عقب یا به چپ و راست تاب میخورد؟",
                        widget=forms.RadioSelect(attrs={'class':'form-check-inline ch'}),choices=CHICES_EXAM2)
    
    q5=forms.ChoiceField(label="به صورت تکرار شونده به اطراف حرکت می کندیا قدم می زند؟(مثلا رفت و برگشت در طول یک اتاق یا در یک مسیر ثابت بیرون از خانه)",
                        widget=forms.RadioSelect(attrs={'class':'form-check-inline ch'}),choices=CHICES_EXAM2)
    
    q6=forms.ChoiceField(label="حرکات تکرار شونده دست و یا انگشت دارد؟(مثلا تکان دادن شدید دست ها یا انگشتان در هوا،دست تکان دادن یا تلنگر زدن با دست به صورت تکرار شونده)",
                        widget=forms.RadioSelect(attrs={'class':'form-check-inline ch'}),choices=CHICES_EXAM2)
    
    q7=forms.ChoiceField(label="شیفتگی خاصی به بعضی اجسام دارد؟(مثلا قطار ،علائم جاده و خیابان و سایر موارد)",
                        widget=forms.RadioSelect(attrs={'class':'form-check-inline ch'}),choices=CHICES_EXAM3)
    
    q8=forms.ChoiceField(label="دوست دارد از زوایای خاص یا غیر معمول به اشیاء نگاه کند؟",
                        widget=forms.RadioSelect(attrs={'class':'form-check-inline ch'}),choices=CHICES_EXAM3)
    
    q9=forms.ChoiceField(label="علاقه خاصی به بوی افراد یا اشیاء دارد؟",
                        widget=forms.RadioSelect(attrs={'class':'form-check-inline ch'}),choices=CHICES_EXAM3)
    
    q10=forms.ChoiceField(label="علاقه خاصی به لمس سطوح مختلف دارد؟",
                        widget=forms.RadioSelect(attrs={'class':'form-check-inline ch'}),choices=CHICES_EXAM3)
    
    q11=forms.ChoiceField(label="چیز خاصی وجود دارد که بخواهد همه جا با خود همراه داشته باشد؟",
                        widget=forms.RadioSelect(attrs={'class':'form-check-inline ch'}),choices=CHICES_EXAM3)
    
    q12=forms.ChoiceField(label="هر چیزی را جمع یا انباشته می کند؟",
                        widget=forms.RadioSelect(attrs={'class':'form-check-inline ch'}),choices=CHICES_EXAM3)
    
    q13=forms.ChoiceField(label="اسرار دارد که چیز هایی در خانه بدون تغییر باقی بمانند؟(مثلا جای قرار گیری مبلمان و وسایل، یا مرتب کردن بعضی چیز ها به شکل ویژه)",
                        widget=forms.RadioSelect(attrs={'class':'form-check-inline ch'}),choices=CHICES_EXAM3)
    
    q14=forms.ChoiceField(label="از ایجاد تغییرات جزئی در چیزها ناراحت می شود؟(مثلا ذرات کثیفی روی لباس ،خط و خراشیدگی جزئی روی اجسام)",
                        widget=forms.RadioSelect(attrs={'class':'form-check-inline ch'}),choices=CHICES_EXAM3)
    
    q15=forms.ChoiceField(label="اسرار دارد که بخش های برنامه ی روزانه اش یکسان و بدون تغییر بماند؟",
                        widget=forms.RadioSelect(attrs={'class':'form-check-inline ch'}),choices=CHICES_EXAM3)
    
    q16=forms.ChoiceField(label="اسرار دارد که کارهارا به شیوه ای خاص انجام دهد یا ترتیب چیز ها را عوض کند تا وقتی (درست) شود؟",
                        widget=forms.RadioSelect(attrs={'class':'form-check-inline ch'}),choices=CHICES_EXAM3)
    
    q17=forms.ChoiceField(label="به صورت تکرار شونده به یک موسیقی گوش میدهد، یک بازی را انجام میدهد،یک ویدئو رو میبنید یا یک کتاب را میخواند؟",
                        widget=forms.RadioSelect(attrs={'class':'form-check-inline ch'}),choices=CHICES_EXAM3)
    
    q18=forms.ChoiceField(label="به پوشیدن یک لباس اسرار دارد یا از پوشیدن لباس جدید خود داری می کند؟",
                        widget=forms.RadioSelect(attrs={'class':'form-check-inline ch'}),choices=CHICES_EXAM3)
    
    q19=forms.ChoiceField(label="آیا بر خوردن یک غذای خاص یا طیف محدودی از غذاها در یک وعده اسرار دارد؟",
                        widget=forms.RadioSelect(attrs={'class':'form-check-inline ch'}),choices=CHICES_EXAM3)
    
    q20=forms.ChoiceField(label="اگر آن ها را به حال خودشان بگذارید، چه نوع فعالیتی را برای سرگرم کردن خودشان انتخاب می کنند؟",
                        widget=forms.RadioSelect(),choices={("1","تقریبا همیشه از مجموعه ای از فعالیت های تکرار شونده انتخاب می کند"),
                                                                                                  ("2","چند موضوع مورد علاقه متفاوت و منعطف اما معمولا فعالیت های مشابه را انتخاب میکند"),
                                                                                                  ("3","مجموعه ای از فعالیت های متنوع و منعطف به انتخاب خود")})
    