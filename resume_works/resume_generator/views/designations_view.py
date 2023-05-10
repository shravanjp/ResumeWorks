from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from ..models import Designation
from ..forms import DesignationForm

@login_required
def designations_list_view(request):
    designations = Designation.objects.filter(is_deleted=False)
    logged_in_user = request.user
    return render(request,'resume_generator/designation/designations_list.html',{
        'designations':designations,
        'logged_in_user': logged_in_user,
    })

@login_required
def create_designation_view(request):
    designations = Designation.objects.filter(is_deleted=False)
    if request.method == 'POST':
        form = DesignationForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            if not Designation.objects.filter(is_deleted=False, name__iexact=name).exists():
                designation_model = Designation(name=name)
                designation_model.save()
                messages.success(request, 'Designation added successfully!')
            else:
                messages.error(request, 'Designation already exists!')
            return redirect('create_designation')

        else:
            messages.info(request, form.errors)
            messages.error(request, 'Invalid form data!')
            return render(request, 'resume_generator/designation/create_designation.html', {'form':form})
    else:
        form = DesignationForm()
        logged_in_user = request.user
        context = {
            'form': form,
            'designations': designations,
            'logged_in_user': logged_in_user,
        }
        return render(request, 'resume_generator/designation/create_designation.html', context)


@login_required
def edit_designation_view(request, designation_id):
    designation = get_object_or_404(Designation, id=designation_id)
    if request.method == 'POST':
        form = DesignationForm(request.POST, instance=designation)
        if form.is_valid():
            name = form.cleaned_data['name']
            if not Designation.objects.filter(is_deleted=False, name__iexact=name).exists():
                form.save()
                messages.success(request, 'Designation updated successfully!')
            else:
                messages.error(request, 'Designation already exists!')
        else:
            messages.error(request,"Invalid Form data")

        return redirect('create_designation')

    else:
        initial_data = {'name': designation.name} 
        form = DesignationForm(instance=designation, initial=initial_data)
        logged_in_user = request.user
        context = {
            'form': form,
            'designation': designation,
            'logged_in_user': logged_in_user,
        }
        return render(request, 'resume_generator/designation/edit_designation.html', context)

@login_required
def delete_designation_view(request, designation_id):
    if request.method == 'POST':
        designation = get_object_or_404(Designation, id=designation_id)
        designation.is_deleted = True
        designation.save()
    return redirect('designations_list')