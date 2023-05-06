from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import *
from .forms import CodingSkillForm, ToolForm
# Create your views here.
@login_required(login_url='accounts/login/')
def home(request):
	return redirect('dashboard/')

#Dashboard
@login_required
def dashboard(request):
    coding_skills_len = len(CodingSkill.objects.filter(is_deleted=False))
    tools_len = len(Tool.objects.filter(is_deleted=False))
    context = {
        'coding_skills_len': coding_skills_len,
        'tools_len': tools_len
    }
    return render(request,'resume_generator/dashboard.html',context)

# Coding Skills
@login_required
def coding_skills_list(request):
    coding_skills = CodingSkill.objects.filter(is_deleted=False)
    return render(request,'resume_generator/coding_skill/coding_skills_list.html',{'coding_skills':coding_skills})

@login_required
def create_coding_skill(request):
    coding_skills = CodingSkill.objects.filter(is_deleted=False)
    if request.method == 'POST':
        form = CodingSkillForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            name = ("").join([x.lower() for x in name]) 

            if not CodingSkill.objects.filter(is_deleted=False, name=name).exists():
                coding_skill_model = CodingSkill(name=name)
                coding_skill_model.save()
                messages.success(request, 'Skill added successfully!')
            else:
                messages.error(request, 'Skill already exists!')
            return redirect('create_coding_skill')

        else:
            messages.info(request, form.errors)
            messages.error(request, 'Invalid form data!')
            # context = {
            #     'form': form,
            #     'skills': skills
            # }
            return render(request, 'resume_generator/coding_skill/create_coding_skill.html', {'form':form})
    else:
        form = CodingSkillForm()
        context = {
            'form': form,
            'coding_skills': coding_skills
        }
        return render(request, 'resume_generator/coding_skill/create_coding_skill.html', context)


@login_required
def edit_coding_skill(request, coding_skill_id):
    coding_skill = get_object_or_404(CodingSkill, id=coding_skill_id)
    print("\n",coding_skill,"\n")
    if request.method == 'POST':
        form = CodingSkillForm(request.POST, instance=coding_skill)
        print(form)
        if form.is_valid():
            name = form.cleaned_data['name']
            name = ("").join([x.lower() for x in name]) 
            if not CodingSkill.objects.filter(is_deleted=False, name=name).exists():
                coding_skill_model = form.save()
                messages.success(request, 'Skill updated successfully!')
            else:
                messages.error(request, 'Skill already exists!')
            return redirect('coding_skills_list')
        else:
            messages.error(request,"Invalid Form data")
            return redirect('coding_skills_list')

    else:
        initial_data = {'name': coding_skill.name} # set initial data for the name field
        form = CodingSkillForm(instance=coding_skill, initial=initial_data)
        context = {
            'form': form,
            'coding_skill': coding_skill,
        }
        return render(request, 'resume_generator/coding_skill/edit_coding_skill.html', context)

@login_required
def delete_coding_skill(request, coding_skill_id):
    if request.method == 'POST':
        coding_skill = get_object_or_404(CodingSkill, id=coding_skill_id)
        coding_skill.is_deleted = True
        coding_skill.save()
    return redirect('coding_skills_list')


#Tools
@login_required
def tools_list(request):
    tools = Tool.objects.filter(is_deleted=False)
    return render(request,'resume_generator/tool/tools_list.html',{'tools':tools})

@login_required
def create_tool(request):
    tools = Tool.objects.filter(is_deleted=False)
    if request.method == 'POST':
        form = ToolForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            name = ("").join([x.lower() for x in name]) 

            if not Tool.objects.filter(is_deleted=False, name=name).exists():
                tool_model = Tool(name=name)
                tool_model.save()
                messages.success(request, 'Tool added successfully!')
            else:
                messages.error(request, 'Tool already exists!')
            return redirect('create_tool')

        else:
            messages.info(request, form.errors)
            messages.error(request, 'Invalid form data!')
            return render(request, 'resume_generator/tool/create_tool.html', {'form':form})
    else:
        form = ToolForm()
        context = {
            'form': form,
            'tools': tools
        }
        return render(request, 'resume_generator/tool/create_tool.html', context)


@login_required
def edit_tool(request, tool_id):
    tool = get_object_or_404(Tool, id=tool_id)
    if request.method == 'POST':
        form = ToolForm(request.POST, instance=tool)
        if form.is_valid():
            name = form.cleaned_data['name']
            name = ("").join([x.lower() for x in name]) 
            if not Tool.objects.filter(is_deleted=False, name=name).exists():
                tool_model = form.save()
                messages.success(request, 'Tool updated successfully!')
            else:
                messages.error(request, 'Skill already exists!')
            return redirect('tools_list')
        else:
            messages.error(request,"Invalid Form data")
            return redirect('tools_list')

    else:
        initial_data = {'name': tool.name} # set initial data for the name field
        form = CodingSkillForm(instance=tool, initial=initial_data)
        context = {
            'form': form,
            'tool': tool,
        }
        return render(request, 'resume_generator/tool/edit_tool.html', context)

@login_required
def delete_tool(request, tool_id):
    if request.method == 'POST':
        tool = get_object_or_404(Tool, id=tool_id)
        tool.is_deleted = True
        tool.save()
    return redirect('tools_list')


    
