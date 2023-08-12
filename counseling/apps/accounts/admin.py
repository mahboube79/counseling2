from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin
from .forms import UserChangeForm , UserCreationForm
from .models import CustomUser

#  ------------------------------------------
class customUserAdmin(UserAdmin):
    form = UserChangeForm
    add_form=UserCreationForm
    
    list_display=('email','name','family','mobile_number','is_active','is_admin')
    
    list_filter=('is_admin',)
    
    fieldsets=(
        (None,{'fields':('email','password')}),
        ('Personal info',{'fields':('name','family','mobile_number')}),
        ('Permissions',{'fields':('is_active','is_admin')})
    )
    
    add_fieldsets=(
         (None,{
            #  'classes':('wide',),
             'fields':('email','name','family','mobile_number','is_active','is_admin','password1','password2'),
         }),
     )
    
    search_fields=('email',)
    ordering=('email',)
    filter_horizontal=()
    
admin.site.register(CustomUser,customUserAdmin)
admin.site.unregister(Group)