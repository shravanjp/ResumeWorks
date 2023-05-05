from django import forms
from .models import CodingSkills, Tools

class CodingSkillForm(forms.ModelForm):
    class Meta:
        model = CodingSkills
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }

# class ToolForm