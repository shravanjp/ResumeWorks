from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from ..models import *
from ..forms import ProjectForm

@login_required
def projects_list_view(request):
    logged_in_user = request.user
    projects = Project.objects.filter(is_deleted=False)
    return render(request,'resume_generator/project/projects_list.html',{
        'projects':projects,
        'logged_in_user': logged_in_user,
    })

@login_required
def create_project_view(request):
    logged_in_user = request.user
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            if not Project.objects.filter(is_deleted=False, name__iexact=name).exists():
                form.save()
                messages.success(request, 'Project added successfully!')
            else:
                messages.error(request, 'Tool already exists!')
            return redirect('create_project')
        else:
            messages.error(request, form.errors)
    else:
        form = ProjectForm()
    return render(request, 'resume_generator/project/create_project.html', {'form': form,'logged_in_user': logged_in_user,})

@login_required
def edit_project_view(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            messages.success(request, 'Project updated successfully!')
            
        else:
            messages.error(request, form.errors)
        return redirect('create_project')
    else:
        form = ProjectForm(instance=project)
        logged_in_user = request.user
    return render(request, 'resume_generator/project/edit_project.html', {'form': form, 'project': project,'logged_in_user': logged_in_user,})


@login_required
def delete_project_view(request, project_id):
    if request.method == 'POST':
        project = get_object_or_404(Project, id=project_id)
        project.is_deleted = True
        project.save()
    return redirect('projects_list')