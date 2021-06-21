from django.contrib import admin

from crudapp.models import Hospital

# Register your models here.


class HospitalAdmin(admin.ModelAdmin):
    list_display=['name','owner','noofdoctors','noofpatients','city','helplineno']




admin.site.register(Hospital,HospitalAdmin)