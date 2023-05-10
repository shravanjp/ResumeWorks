from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from ..models import *
from ..forms import ToolForm
from ..forms import ProjectForm

@login_required
def projects_list_view(request):
    projects = Project.objects.filter(is_deleted=False)
    return render(request,'resume_generator/project/projects_list.html',{'projects':projects})

@login_required
def create_project_view(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            # Optionally add a success message
            return redirect('create_project')
        else:
            messages.error(request, form.errors)
    else:
        form = ProjectForm()
    return render(request, 'resume_generator/project/create_project.html', {'form': form})


    # projects = Project.objects.filter(is_deleted=False)
    # if request.method == 'POST':
    #     form = ProjectForm(request.POST)
    #     if form.is_valid():
    #         name = form.cleaned_data['name']
    #         name = ("").join([x.lower() for x in name]) 

    #         if not Tool.objects.filter(is_deleted=False, name=name).exists():
    #             tool_model = Tool(name=name)
    #             tool_model.save()
    #             messages.success(request, 'Tool added successfully!')
    #         else:
    #             messages.error(request, 'Tool already exists!')
    #         return redirect('create_project')

    #     else:
    #         messages.info(request, form.errors)
    #         messages.error(request, 'Invalid form data!')
    #         return render(request, 'resume_generator/project/create_project.html', {'form':form})
    # else:
    #     form = ToolForm()
    #     context = {
    #         'form': form,
    #         'projects': projects
    #     }
    # return render(request, 'resume_generator/project/create_project.html')


@login_required
def edit_project_view(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('create_project')
    else:
        form = ProjectForm(instance=project)
    return render(request, 'resume_generator/project/edit_project.html', {'form': form, 'project': project})

# def edit_project_view(request, tool_id):
#     tool = get_object_or_404(Tool, id=tool_id)
#     if request.method == 'POST':
#         form = ToolForm(request.POST, instance=tool)
#         if form.is_valid():
#             name = form.cleaned_data['name']
#             name = ("").join([x.lower() for x in name]) 
#             if not Tool.objects.filter(is_deleted=False, name=name).exists():
#                 tool_model = form.save()
#                 messages.success(request, 'Tool updated successfully!')
#             else:
#                 messages.error(request, 'Skill already exists!')
#             return redirect('tools_list')
#         else:
#             messages.error(request,"Invalid Form data")
#             return redirect('tools_list')

#     else:
#         initial_data = {'name': tool.name} # set initial data for the name field
#         form = ToolForm(instance=tool, initial=initial_data)
#         context = {
#             'form': form,
#             'tool': tool,
#         }
#         return render(request, 'resume_generator/tool/edit_tool.html', context)

@login_required
def delete_project_view(request, project_id):
    if request.method == 'POST':
        project = get_object_or_404(Project, id=project_id)
        project.is_deleted = True
        project.save()
    return redirect('projects_list')