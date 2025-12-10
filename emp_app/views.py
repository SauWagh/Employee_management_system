from django.shortcuts import render,redirect,get_object_or_404
from emp_app.models import Employee
import uuid
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse

# Create your views here.

def gen_emp_id():
    return str(uuid.uuid4())

def home(request):
    return render(request, 'emp_app/home.html')


# --------------add employee data---------------
def add_emp_data(request):

    if request.method == 'POST':
        # employe_id = request.POST.get('eemp_id')
        name =request.POST.get('ename')
        mobile_num = request.POST.get('emob_num')
        address = request.POST.get('eadd')
        designation = request.POST.get('edes')
        working = request.POST.get('ework') == 'on'
        gender = request.POST.get('egender')
        email_id = request.POST.get('eemail_id')
        salary = request.POST.get('esal')

        Employee.objects.create(
            name = name,
            mobile_num = mobile_num,
            address = address,
            designation = designation,
            # employe_id = employe_id,
            working = working,
            gender = gender,
            email_id = email_id,
            salary = salary,
        )
        return redirect('/forms/emp_table/')
    
    return render(request, 'emp_app/add.html',{'emp_table' : gen_emp_id()})



#----------------employee table---------------------------------
def emp_table(request):
    query = request.GET.get('q','')
    employee = Employee.objects.filter(name__icontains= query) if query else Employee.objects.all()
    # employe_table = Employee.objects.all()

    return render(request,'emp_app/emp_table.html/',{'employe_table':employee})


# ------------------------ employee lsit -------------------------------
def emp_list(request):
    search = request.GET.get('q','')
    if search:
        emp_list = Employee.objects.filter(name__icontains = search)
    else:
        emp_list = Employee.objects.all()
    return render(request, 'emp_app/emp_list.html',{'emp_list':emp_list})


# ---------------------employee Detail -----------------------------------
def emp_detail(request,employe_id):

    employee = get_object_or_404(Employee, employe_id = employe_id)

    return render(request, 'emp_app/emp_detail.html',{'obj':employee})

# --------------------Employee delete------------------------

def delete(request,employe_id):
    obj = Employee.objects.get(employe_id = employe_id)
    
    if request.method == 'POST':
        obj.delete()
        return redirect('/emp_table')
    
    # emp_del = get_object_or_404(Employee,employe_id = employe_id)
    return render(request,'emp_app/delete.html',{'obj':obj})

# --------------------Update Employee----------------------------------

def emp_update(request,employe_id):
    obj = get_object_or_404(Employee,employe_id = employe_id)

    if request.method == 'POST':
        update_name         =   request.POST.get('u_name')
        update_mobile_num   =   request.POST.get('u_mob_num')
        update_address      =   request.POST.get('u_adderess')
        update_designation  =   request.POST.get('u_designation')
        update_working      =   request.POST.get('u_working') == 'on'
        update_gender       =   request.POST.get('u_gender')
        update_email_id     =   request.POST.get('u_email_id')
        update_salary       =   request.POST.get('u_salary')

        if not update_name:
            return render(request, 'emp_app/update.html/',{
                'employee' : obj,
                'error' :'Name is required.'
                })


        obj.name        = update_name
        obj.mobile_num  = update_mobile_num
        obj.address     = update_address
        obj.designation = update_designation
        obj.working     = update_working
        obj.gender      = update_gender
        obj.email_id    = update_email_id
        obj.salary      = update_salary

        obj.save()
        print("Redirecting to:", f'/emp_detail/{obj.employe_id}/')

        return redirect(f'/emp_detail/{obj.employe_id}/')
    print(Employee.objects.filter(employe_id=obj.employe_id).exists())

        # return redirect(reverse('emp_detail', args=[obj.employe_id]))
    
    return render(request,'emp_app/update.html',{'obj':obj})