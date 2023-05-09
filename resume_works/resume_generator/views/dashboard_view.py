from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from ..models import CodingSkill, Tool, Project

@login_required(login_url='accounts/login/')
def home_view(request):
	return redirect('dashboard/')

#Dashboard
@login_required
def dashboard_view(request):
    coding_skills_len = len(CodingSkill.objects.filter(is_deleted=False))
    tools_len = len(Tool.objects.filter(is_deleted=False))
    projects_len = len(Project.objects.filter(is_deleted=False))
    employees_len = 0
    context = {
        'coding_skills_len': coding_skills_len,
        'tools_len': tools_len,
        'projects_len' : projects_len,
        'employees_len' : employees_len,
    }
    return render(request,'resume_generator/dashboard.html',context)