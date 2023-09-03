from django.urls import path
from . import views

app_name='main'
urlpatterns=[
    path('',views.MainView.as_view(),name="index"),
    path('showblog/',views.showblog,name="showblog"),
    path('registerblog/',views.create_blog,name="registerblog"),
    path('mainblog/',views.mainblog,name="mainblog"),
    path('aboutus/',views.aboutus,name="aboutus"),
    path('consultant/',views.consultant,name="consultant"),
    path('videos/',views.videos,name="videos"),
    path('create_video/',views.create_video,name="create_video"),
    
    

]