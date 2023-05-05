from django.shortcuts import render, redirect
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
def skills_list(request):
    coding_skills = CodingSkills.objects.all()
    return render(request,'resume_generator/skills_list.html',{'coding_skills':coding_skills})

@login_required
def create_skill(request):
    coding_skills = CodingSkills.objects.all()
    if request.method == 'POST':
        form = CodingSkillForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            name = ("").join([x.lower() for x in name]) 

            if not CodingSkills.objects.filter(name=name).exists():
                coding_skill_model = CodingSkills(name=name)
                coding_skill_model.save()
                messages.success(request, 'Skill added successfully!')
            else:
                messages.error(request, 'Skill already exists!')
            return redirect('create_skill')

        else:
            messages.info(request, form.errors)
            messages.error(request, 'Invalid form data!')
            # context = {
            #     'form': form,
            #     'skills': skills
            # }
            return render(request, 'resume_generator/create_skill.html', {'form':form})
    else:
        print("2nd part")
        form = CodingSkillForm()
        context = {
            'form': form,
            'coding_skills': coding_skills
        }
        return render(request, 'resume_generator/create_skill.html', context)


