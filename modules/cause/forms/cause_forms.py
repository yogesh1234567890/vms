from django import forms
from modules.cause.models.cause_models import cause

class causeForm(forms.ModelForm):
    class Meta:
        model = cause
        fields=['name','description','date','volunteer_no','status']