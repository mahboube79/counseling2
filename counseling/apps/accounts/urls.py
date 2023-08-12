from django.urls import path
from . import views

app_name='accounts'
urlpatterns=[
    path('register/',views.RegisterUserView.as_view(),name="register"),
    path('login/',views.LoginUserView.as_view(),name="login"),
    path('logout/',views.LogoutUserView.as_view(),name="logout"),
] 