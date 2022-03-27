from django import forms
from .models import  imagetopdf
from django.forms import ClearableFileInput, FileInput




class ImagePDF(forms.ModelForm):
     def __init__(self, *args, **kwargs):
         kwargs.setdefault('label_suffix', '')
         super(ImagePDF, self).__init__(*args, **kwargs)
    
     class Meta:
        model = imagetopdf
        labels = {
            'money': 'Enter Amount',
        }
        fields = ['money']

        widgets = {
            'id':'btn3',
            
        }
 