from django import forms
from .models import Blog,BlogGallery

class BlogForm(forms.ModelForm):
    class Meta:
        model=Blog
        fields=['blog_title','blog_text',]
        
        
class BlogGalleryForm(forms.ModelForm):
    class Meta:
        model=BlogGallery
        fields=['blog_image_name',]