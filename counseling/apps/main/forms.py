from django import forms
from .models import *

class BlogForm(forms.ModelForm):
    class Meta:
        model=Blog
        fields=['blog_title','blog_text','blog_summery','main_img',]
        


class VideoForm(forms.ModelForm):
    class Meta:
        model=Videos
        fields=['title','video','poster']