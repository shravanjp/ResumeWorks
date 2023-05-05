from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import *
from .forms import SkillForm
# Create your views here.
@login_required(login_url='accounts/login/')
def home(request):
	return redirect('dashboard/')

@login_required
def dashboard(request):
	return render(request,'resume_generator/dashboard.html')

@login_required
def skills_list(request):
    skills = Skill.objects.all()
    return render(request,'resume_generator/skills_list.html',{'skills':skills})

@login_required
def add_skill(request):
    skills = Skill.objects.all()
    if request.method == 'POST':
        form = SkillForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            name = ("").join([x.lower() for x in name]) 

            if not Skill.objects.filter(name=name).exists():
                skill_model = Skill(name=name)
                skill_model.save()
                messages.success(request, 'Skill added successfully!')
            else:
                messages.error(request, 'Skill already exists!')
            return redirect('add_skill')

        else:
            messages.info(request, form.errors)
            messages.error(request, 'Invalid form data!')
            # context = {
            #     'form': form,
            #     'skills': skills
            # }
            return render(request, 'resume_generator/add_skill.html', {'form':form})
    else:
        print("2nd part")
        form = SkillForm()
        context = {
            'form': form,
            'skills': skills
        }
        return render(request, 'resume_generator/add_skill.html', context)
