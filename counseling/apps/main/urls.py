from django.urls import path
from . import views

app_name='main'
urlpatterns=[
    path('',views.MainView.as_view(),name="index"),
    path('showblog/',views.showblog,name="showblog"),
    path('registerblog/',views.create_blog,name="registerblog"),   
]