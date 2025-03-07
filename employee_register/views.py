from django.shortcuts import render, redirect
from .forms import EmployeeForm
from .models import Employee

# Create your views here.

# function to retrieve and display all of the employing details (Retrieve Operation)
def employee_list(request):
    context = { 'employee_list': Employee.objects.all() }
    return render(request, "employee_register/employee_list.html",context)

# function handling the form (insert and update operation)
def employee_form(request, id=0):
    if request.method == "GET":
        if id==0:
            form = EmployeeForm()
        else:
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(instance=employee)
        return render(request, "employee_register/employee_form.html", {'form': form})
    else:
        if id == 0:
            form = EmployeeForm(request.POST)
        else:
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(request.POST, instance= employee)
        if form.is_valid():
            form.save()
        return redirect('/employee/lists')
# function handling deleting of employees (Delete Operations)
def employee_delete(request, id):
    employee = Employee.objects.get(pk=id)
    employee.delete()
    return redirect('/employee/lists')