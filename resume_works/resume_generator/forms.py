from django import forms
from .models import CodingSkill, Tool, Designation, Project, Employee

class CodingSkillForm(forms.ModelForm):
    class Meta:
        model = CodingSkill
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }

class ToolForm(forms.ModelForm):
    class Meta:
        model = Tool
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }

class DesignationForm(forms.ModelForm):
    class Meta:
        model = Designation
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'description', 'tools_used', 'coding_skills_used', 'roles_responsibility', 'start_date', 'end_date', 'status']

    name = forms.CharField(label='Name', max_length=255)
    description = forms.CharField(label='Description', widget=forms.Textarea)
    tools_used = forms.ModelMultipleChoiceField(queryset=Tool.objects.all(), widget=forms.CheckboxSelectMultiple)
    coding_skills_used = forms.ModelMultipleChoiceField(queryset=CodingSkill.objects.all(), widget=forms.CheckboxSelectMultiple)
    roles_responsibility = forms.CharField(label='Roles and Responsibilities', widget=forms.Textarea)
    start_date = forms.DateField(label='Start Date', widget=forms.TextInput(attrs={'type': 'date'}))
    end_date = forms.DateField(label='End Date', required=False, widget=forms.TextInput(attrs={'type': 'date'}),initial="In Progress")
    status = forms.ChoiceField(label='Status', choices=Project.PROJECT_STATUS_CHOICES, widget=forms.RadioSelect)

    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get("start_date")
        end_date = cleaned_data.get("end_date")
        status = cleaned_data.get("status")
        if status == 'active' and end_date is None:
            raise forms.ValidationError("End date is required for active projects.")
        elif status == 'close' and end_date is not None and end_date < start_date:
            raise forms.ValidationError("End date cannot be before start date.")

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['name','designation','professional_summary','coding_skills','tools','employment_status']

class EmployeeProjectMappingForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['projects'].queryset = Project.objects.filter(is_deleted=False)
    class Meta:
        model = Employee
        fields = ['projects']
        widget={
            'projects' : forms.CheckboxSelectMultiple(attrs={'class': 'project-checkbox'})
        }

