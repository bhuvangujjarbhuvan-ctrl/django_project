from django.shortcuts import render
from .models import Employee

#Create your views here.

def home (request):
    """ Renders the home page for Employee app"""
    return render (request, 'home.html')

#Additional views for employee operations can be added here

def add_employee (request):
    """View to add a new employee"""
    if request.method == "POST":
        employee_name = request.POST['emp_name']
        employee_age = request.POST['emp_age']
        employee_address = request.POST['emp_address']
        employee_department = request.POST['emp_department']
        employee_reporting_manager =request.POST['emp_reporting_manager']
        employee_email=request.POST['emp_email']
        # creating a class in the object
        employee_data = Employee(employee_name = employee_name, employee_age = employee_age, 
        employee_address = employee_address, employee_department = employee_department,
        employee_reporting_manager = employee_reporting_manager,
        employee_email = employee_email)
        employee_data.save()
        return render(request,'message.html',context={
            'msg':'employee data added successfully'
        })
    return render(request, 'employee/add.html')

def edit_employee (request, emp_id):
    """ View to edit an existing employee HWH"""
    employee=Employee.objects.get(id=emp_id)
    if request.method=="POST":
        employee.employee_name=request.POST['emp_name']
        employee.employee_age=request.POST['emp_age']
        employee.employee_address=request.POST['emp_address']
        employee.employee_department = request.POST['emp_department']
        employee.employee_reporting_manager =request.POST['emp_reporting_manager']
        employee.employee_email=request.POST['emp_email']
        employee.save()
        return render(request,'message.html',context={'msg': 'Employee data update succesfully!!'})
    return render(request, 'employee/edit.html', context={ 'employee': employee })

def delete_employee(request, emp_id): 
    """view to delete an employee"""
    employee = Employee.objects.get(id = emp_id)
    employee.delete()
    return render(request, 'message.html', context={
        'msg':'employee data deleted successfully'})

def employee_detail(request, emp_id):
    """ View to see details of a specific employee"""
    employee= Employee.objects.get(id=emp_id)
    return render(request, 'employee/view.html', {'employee': employee})

def employee_list(request):
    """ View to list all employees"""
    employees=Employee.objects.all()
    return render(request, 'employee/view_id.html',context={'employees':employees})