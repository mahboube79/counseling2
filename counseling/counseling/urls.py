from django.contrib import admin
from django.urls import path , include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('apps.main.urls',namespace='main')),
    path('accounts/',include('apps.accounts.urls',namespace='accounts')),
    path('exam/',include('apps.exam.urls',namespace='exam')),
    
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
