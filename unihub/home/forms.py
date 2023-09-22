from django import forms
from django.forms import ModelForm, TextInput, EmailInput
from .models import *
  
class projects_form(forms.ModelForm):
  
    class Meta:
        model = projects
        fields = ['student_name', 'project_content','project_title','project_domain','project_content','university_name','student_photo','project_cover']
        # widgets = {
        #     'student_name': TextInput(attrs={
        #         'class': "form-control",
        #         'style': 'max-width: 300px;',
        #         'placeholder': 'student_name'
        #         }),
        #     'project_content': EmailInput(attrs={
        #         'class': "form-control", 
        #         'style': 'max-width: 300px;',
        #         'placeholder': 'project_content'
        #         }),
        #     'project_title': TextInput(attrs={
        #         'class': "form-control",
        #         'style': 'max-width: 300px;',
        #         'placeholder': 'project_title'
        #         }),
        #     'project_domain': TextInput(attrs={
        #         'class': "form-control",
        #         'style': 'max-width: 300px;',
        #         'placeholder': 'project_domain'
        #         }),
        #     'project_content': TextInput(attrs={
        #         'class': "form-control",
        #         'style': 'max-width: 300px;',
        #         'placeholder': 'project_content'
        #         }),
        #     'university_name': TextInput(attrs={
        #         'class': "form-control",
        #         'style': 'max-width: 300px;',
        #         'placeholder': 'Namuniversity_namee'
        #         }),
        #      'student_photo': TextInput(attrs={
        #         'class': "form-control",
        #         'style': 'max-width: 300px;',
        #         # 'placeholder': 'Nastudent_photome'
        #         }),
        #     'project_cover': TextInput(attrs={
        #         'class': "form-control",
        #         'style': 'max-width: 300px;',
        #         # 'placeholder': 'project_cover'
        #         }),

        # }