from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from ..models import CodingSkill, Tool, Project, Employee

@login_required(login_url='accounts/login/')
def home_view(request):
    return redirect('dashboard/')

#Dashboard
@login_required
def dashboard_view(request):
    coding_skills_len = len(CodingSkill.objects.filter(is_deleted=False))
    tools_len = len(Tool.objects.filter(is_deleted=False))
    projects_len = len(Project.objects.filter(is_deleted=False))
    employees_len = len(Employee.objects.filter(is_deleted=False))
    logged_in_user = request.user
    
    context = {
        'coding_skills_len': coding_skills_len,
        'tools_len': tools_len,
        'projects_len' : projects_len,
        'employees_len' : employees_len,
        'logged_in_user': logged_in_user,
    }
    return render(request,'resume_generator/dashboard.html',context)




# def users_list_view(request):
#     users = User.objects.all()
#     return render(request, 'resume_generator/user/users_list.html', {'users': users})