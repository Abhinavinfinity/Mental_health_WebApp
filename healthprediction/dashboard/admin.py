from django.contrib import admin
from .models import Data

# Register your models here.
class DataAdmin(admin.ModelAdmin):
    list_display=('name','country','state','tech_company','student','physical_health','age','sex','family_history','predictions')
admin.site.register(Data,DataAdmin)
