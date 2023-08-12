from django import forms
from .models import CustomUser
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError
# ------------------------------------------------
class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)
    
    class Meta:
      model = CustomUser
      fields = ('email','name','family','mobile_number')
      
    def clean_password2(self):
        password1= self.cleaned_data.get("password1")
        password2= self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("passwords do not match")  
        return password1
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user
# ------------------------------------------------
class UserChangeForm(forms.ModelForm):
    password=ReadOnlyPasswordHashField(help_text="برای تغییر رمز <a href='../password'> کلیک </a> کنید")
    class Meta:
        model=CustomUser
        fields=('email','password','name','family','mobile_number','gender','is_active','is_admin')
        
# ------------------------------------------------
class RegisterUserForm(forms.Form):
    email=forms.EmailField(label="",
                           error_messages={'required':'این فیلد نباید خالی باشد',
                                           'invalid':'ایمیل وارد شده نامعتبر می باشد'},
                           widget=forms.TextInput(attrs={'class':'form-control','placeholder':'ایمیل خود را وارد کنید'}))
    name=forms.CharField(label="",
                         widget=forms.TextInput(attrs={'class':'form-control','placeholder':'نام خود را وارد کنید'}))
    family=forms.CharField(label="",
                           widget=forms.TextInput(attrs={'class':'form-control','placeholder':'نام خانوادگی خود را وارد کنید'}))
    mobile_number=forms.CharField(label="",
                                  widget=forms.TextInput(attrs={'class':'form-control','placeholder':'شماره تماس خود را وارد کنید'}))
    password=forms.CharField(label="",
                             widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'رمز عبور '}))
    confirm_password=forms.CharField(label="",
                                     widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'تکرار رمز عبور'}))
    
    
#<-------- check the email and number not Repetitious  ----------->  
    def clean_email(self):
        email=self.cleaned_data['email']
        flag=CustomUser.objects.filter(email=email).exists()
        if flag:
            raise ValidationError('ایمیل وارد شده قبلا در سیستم ثبت شده است!')
        return email
    
    def clean_mobile_number(self):
        mobile_number=self.cleaned_data['mobile_number']
        flag=CustomUser.objects.filter(mobile_number=mobile_number).exists()
        if flag:
            raise ValidationError('شماره موبایل وارد شده قبلا در سیستم ثبت  شده است')
        return mobile_number
    def clean(self):
        password=self.cleaned_data.get('password')
        confirm_password=self.cleaned_data.get('confirm_password')
        if password and confirm_password and password != confirm_password:
            raise ValidationError('رمزعبور و تکرار رمز عبور باهم مغایرت دارند')
    
# -----------------------------------------------
class LoginUserForm(forms.Form):
    email = forms.EmailField(label="",
                             error_messages={'required':'این فیلد نباید خالی باشد',
                                           'invalid':'ایمیل وارد شده نامعتبر می باشد'},
                             widget=forms.TextInput(attrs={'class':'form-control','placeholder':'ایمیل خود را وارد کنید'}))  
    password=forms.CharField(label="",
                             widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'رمز عبور '}))


 