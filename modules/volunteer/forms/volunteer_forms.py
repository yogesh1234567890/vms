from django import forms

from modules.volunteer.models.volunteer_models import volunteerRegistration

class volunteerForm(forms.ModelForm):
    class Meta:
        model = volunteerRegistration

        fields = ['first_name','last_name','email','address','contact_no','skills']
