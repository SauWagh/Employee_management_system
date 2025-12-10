from django.contrib import admin
from emp_app.models import Employee

# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['employe_id', 'name', 'designation', 'email_id','working','mobile_num','gender']
    search_fields = ['name', 'email_id', 'employe_id']
    # list_filter = ['designation', 'gender', 'working']

    
admin.site.register(Employee,EmployeeAdmin)
