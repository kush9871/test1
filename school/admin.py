from django.contrib import admin
from school.models import *
# Register your models here.


class Classname(admin.ModelAdmin):
    list_display=('id','stuid','stuname','sturoll','stumail','stupass','datetime')

class Classname2(admin.ModelAdmin):
    list_display=('n','m','p')


admin.site.register(Form,Classname)
admin.site.register(Formvalidation,Classname2)
