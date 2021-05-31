from django import forms
from .models import ResumeSection


class UploadForm(forms.ModelForm):
    class Meta:
        model = ResumeSection
        fields = ('full_name', 'email', 'address', 'phone','resume','position','title','strength')

        