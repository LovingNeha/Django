from django.contrib import admin
from.models import Department,Employee

# Register your models here.
admin.site.register(Department)
#admin.site.register(Employee)
#we can also use decorator at the place of above line for admin

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
   list_display = ("first_name","position","Depart")
   search_fields = ["position"]

