from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import *
from .forms import CodingSkillForm
# Create your views here.
@login_required(login_url='accounts/login/')
def home(request):
	return redirect('dashboard/')

@login_required
def dashboard(request):
	return render(request,'resume_generator/dashboard.html')

@login_required
def coding_skills_list(request):
    coding_skills = CodingSkill.objects.filter(is_deleted=False)
    return render(request,'resume_generator/coding_skills_list.html',{'coding_skills':coding_skills})

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
            return render(request, 'resume_generator/create_coding_skill.html', {'form':form})
    else:
        form = CodingSkillForm()
        context = {
            'form': form,
            'coding_skills': coding_skills
        }
        return render(request, 'resume_generator/create_coding_skill.html', context)


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
                # coding_skill_model = CodingSkill(name=name)
                # coding_skill_model.save()
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
        return render(request, 'resume_generator/edit_coding_skill.html', context)
    # coding_skill = get_object_or_404(CodingSkill, id=coding_skill_id)
    # if request.method == 'POST':
    #     form = CodingSkillForm(request.POST, instance=coding_skill)
    #     if form.is_valid():
    #         name = form.cleaned_data['name']
    #         name = ("").join([x.lower() for x in name]) 

    #         if not CodingSkill.objects.filter(is_deleted=False, name=name).exists():
    #             coding_skill_model = CodingSkill(name=name)
    #             coding_skill_model.save()
    #             messages.success(request, 'Skill added successfully!')
    #         else:
    #             messages.error(request, 'Skill already exists!')
    #         return redirect('coding_skill_list')
    #     else:
    #         messages.info(request, form.errors)
    #         return render(request, 'resume_generator/edit_coding_skill.html', {'form':form})
    # else:
    #     form = CodingSkillForm(instance=coding_skill)
    #     return redirect('coding_skills_list')


@login_required
def delete_coding_skill(request, coding_skill_id):
    if request.method == 'POST':
        coding_skill = get_object_or_404(CodingSkill, id=coding_skill_id)
        coding_skill.is_deleted = True
        coding_skill.save()
    return redirect('coding_skills_list')

    
