from django import forms
from .models import CodingSkill, Tool

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