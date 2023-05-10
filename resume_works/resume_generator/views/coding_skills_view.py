from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from ..models import CodingSkill
from ..forms import CodingSkillForm


@login_required
def coding_skills_list_view(request):
    coding_skills = CodingSkill.objects.filter(is_deleted=False)
    logged_in_user = request.user
    return render(request,'resume_generator/coding_skill/coding_skills_list.html',{
        'coding_skills':coding_skills,
        'logged_in_user': logged_in_user,
    })

@login_required
def create_coding_skill_view(request):
    coding_skills = CodingSkill.objects.filter(is_deleted=False)
    if request.method == 'POST':
        form = CodingSkillForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']

            if not CodingSkill.objects.filter(is_deleted=False, name__iexact=name).exists():
                coding_skill_model = CodingSkill(name=name)
                coding_skill_model.save()
                messages.success(request, 'Skill added successfully!')
            else:
                messages.error(request, 'Skill already exists!')
            return redirect('create_coding_skill')

        else:
            messages.info(request, form.errors)
            messages.error(request, 'Invalid form data!')
            return render(request, 'resume_generator/coding_skill/create_coding_skill.html', {'form':form})
    else:
        form = CodingSkillForm()
        logged_in_user = request.user
        context = {
            'form': form,
            'coding_skills': coding_skills,
            'logged_in_user': logged_in_user,
        }
        return render(request, 'resume_generator/coding_skill/create_coding_skill.html', context)


@login_required
def edit_coding_skill_view(request, coding_skill_id):
    coding_skill = get_object_or_404(CodingSkill, id=coding_skill_id)
    print("\n",coding_skill,"\n")
    if request.method == 'POST':
        form = CodingSkillForm(request.POST, instance=coding_skill)
        print(form)
        if form.is_valid():
            name = form.cleaned_data['name']
            if not CodingSkill.objects.filter(is_deleted=False, name__iexact=name).exists():
                coding_skill_model = form.save()
                messages.success(request, 'Skill updated successfully!')
            else:
                messages.error(request, 'Skill already exists!')
            return redirect('create_coding_skill')
        else:
            messages.error(request,"Invalid Form data")
            return redirect('create_coding_skill')

    else:
        initial_data = {'name': coding_skill.name} # set initial data for the name field
        form = CodingSkillForm(instance=coding_skill, initial=initial_data)
        logged_in_user = request.user
        context = {
            'form': form,
            'coding_skill': coding_skill,
            'logged_in_user': logged_in_user,
        }
        return render(request, 'resume_generator/coding_skill/edit_coding_skill.html', context)

@login_required
def delete_coding_skill_view(request, coding_skill_id):
    if request.method == 'POST':
        coding_skill = get_object_or_404(CodingSkill, id=coding_skill_id)
        coding_skill.is_deleted = True
        coding_skill.save()
    return redirect('coding_skills_list')