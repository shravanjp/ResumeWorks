from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from ..models import *
from ..forms import EmployeeForm, EmployeeProjectMappingForm

@login_required
def employees_list_view(request):
    logged_in_user = request.user
    employees = Employee.objects.filter(is_deleted=False)
    return render(request,'resume_generator/employee/employees_list.html',{
        'employees': employees,
        'logged_in_user': logged_in_user,
    })

@login_required
def create_employee_view(request):
    logged_in_user = request.user
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        print("\n\n",form.fields,"\n\n")
        if form.is_valid():
            name = form.cleaned_data['name']
            if not Employee.objects.filter(is_deleted=False, name__iexact=name).exists():
                form.save()
                messages.success(request, 'Employee added successfully!')
            else:
                messages.error(request, 'Employee already exists!')
            return redirect('create_employee')
        else:
            messages.error(request, form.errors)
    else:
        form = EmployeeForm()
        return render(request, 'resume_generator/employee/create_employee.html', {'form': form,'logged_in_user': logged_in_user,
})

@login_required
def edit_employee_view(request, employee_id):
    employee = get_object_or_404(Employee, id=employee_id)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            messages.success(request, 'Employee updated successfully!')
            
        else:
            messages.error(request, form.errors)
        return redirect('create_employee')
    else:
        form = EmployeeForm(instance=employee)
        logged_in_user = request.user
    return render(request, 'resume_generator/employee/edit_employee.html', {'form': form, 'employee': employee,'logged_in_user': logged_in_user,})


@login_required
def delete_employee_view(request, employee_id):
    if request.method == 'POST':
        employee = get_object_or_404(Employee, id=employee_id)
        employee.is_deleted = True
        employee.save()
    return redirect('employees_list')

@login_required
def map_employee_to_projects_view(request, employee_id):
    logged_in_user = request.user
    employee = get_object_or_404(Employee, id=employee_id)
    if request.method == 'POST':
        form = EmployeeProjectMappingForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            messages.success(request, 'Mapped successfully!')
        return redirect('employees_list')
    else:
        form = EmployeeProjectMappingForm(instance=employee)
        return render(request,'resume_generator/employee/map_to_projects.html/', {
            'form': form, 
            'employee': employee,
            'logged_in_user': logged_in_user,
        })

@login_required
def employee_resume_view(request, employee_id):
    logged_in_user = request.user
    employee = get_object_or_404(Employee, id=employee_id)
    projects = projects = employee.projects.all()
    context = {
        'employee':employee,
        'projects':projects,
        'ename':'dummy',
    }
    return render(request, 'resume_generator/employee/view_resume.html', context)
  