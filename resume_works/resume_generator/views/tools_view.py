from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from ..models import Tool
from ..forms import ToolForm


@login_required
def tools_list_view(request):
    tools = Tool.objects.filter(is_deleted=False)
    logged_in_user = request.user
    return render(request,'resume_generator/tool/tools_list.html',{'tools':tools,'logged_in_user': logged_in_user,})

@login_required
def create_tool_view(request):
    tools = Tool.objects.filter(is_deleted=False)
    if request.method == 'POST':
        form = ToolForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            if not Tool.objects.filter(is_deleted=False, name__iexact=name).exists():
                tool_model = Tool(name=name)
                tool_model.save()
                messages.success(request, 'Tool added successfully!')
            else:
                messages.error(request, 'Tool already exists!')
            return redirect('create_tool')

        else:
            messages.info(request, form.errors)
            messages.error(request, 'Invalid form data!')
            return render(request, 'resume_generator/tool/create_tool.html', {'form':form,'logged_in_user': logged_in_user,})
    else:
        form = ToolForm()
        logged_in_user = request.user
        context = {
            'form': form,
            'tools': tools,
            'logged_in_user': logged_in_user,
        }
        return render(request, 'resume_generator/tool/create_tool.html', context)


@login_required
def edit_tool_view(request, tool_id):
    tool = get_object_or_404(Tool, id=tool_id)
    if request.method == 'POST':
        form = ToolForm(request.POST, instance=tool)
        if form.is_valid():
            name = form.cleaned_data['name']
            if not Tool.objects.filter(is_deleted=False, name__iexact=name).exists() :
                form.save()
                messages.success(request, 'Tool updated successfully!')
            else:
                
                messages.error(request, 'Skill already exists!')
            return redirect('create_tool')
        else:
            messages.error(request,"Invalid Form data")
            return redirect('create_tool')

    else:
        initial_data = {'name': tool.name} # set initial data for the name field
        form = ToolForm(instance=tool, initial=initial_data)
        logged_in_user = request.user
        context = {
            'form': form,
            'tool': tool,
            'logged_in_user': logged_in_user,
        }
        return render(request, 'resume_generator/tool/edit_tool.html', context)

@login_required
def delete_tool_view(request, tool_id):
    if request.method == 'POST':
        tool = get_object_or_404(Tool, id=tool_id)
        tool.is_deleted = True
        tool.save()
    return redirect('tools_list')