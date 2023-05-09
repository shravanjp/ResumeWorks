from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from ..models import Designation
from ..forms import DesignationForm


@login_required
def designations_list_view(request):
    designations = Designation.objects.filter(is_deleted=False)
    return render(request,'resume_generator/designation/designations_list.html',{'designations':designations})

@login_required
def create_designation_view(request):
    designations = Designation.objects.filter(is_deleted=False)
    if request.method == 'POST':
        form = DesignationForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            name = ("").join([x.lower() for x in name]) 

            if not Designation.objects.filter(is_deleted=False, name=name).exists():
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
        context = {
            'form': form,
            'designations': designations
        }
        return render(request, 'resume_generator/designation/create_designation.html', context)


@login_required
def edit_designation_view(request, designation_id):
    designation = get_object_or_404(Designation, id=designation_id)
    if request.method == 'POST':
        form = DesignationForm(request.POST, instance=designation)
        if form.is_valid():
            name = form.cleaned_data['name']
            name = ("").join([x.lower() for x in name]) 
            if not Designation.objects.filter(is_deleted=False, name=name).exists():
                form.save()
                messages.success(request, 'Designation updated successfully!')
            else:
                messages.error(request, 'Designation already exists!')
        else:
            messages.error(request,"Invalid Form data")

        return redirect('create_designation')

    else:
        initial_data = {'name': designation.name} # set initial data for the name field
        form = DesignationForm(instance=designation, initial=initial_data)
        context = {
            'form': form,
            'designation': designation,
        }
        return render(request, 'resume_generator/designation/edit_designation.html', context)

@login_required
def delete_designation_view(request, designation_id):
    if request.method == 'POST':
        designation = get_object_or_404(Designation, id=designation_id)
        designation.is_deleted = True
        designation.save()
    return redirect('designations_list')