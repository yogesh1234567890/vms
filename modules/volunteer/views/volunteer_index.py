from django.conf import settings
from django.shortcuts import render, HttpResponse,redirect
from django.core.mail import send_mail
from modules.volunteer.models.volunteer_models import volunteerRegistration
from modules.volunteer.forms.volunteer_forms import volunteerForm


def index(request):
    form = volunteerForm()
    if (request.method == 'POST'):
        form = volunteerForm(request.POST)
        if (form.is_valid()):
            subject = 'test'
            message = 'thank you for registering...'
            mailer = settings.EMAIL_HOST_USER
            send_to = request.POST['email']
            send_mail(subject,message,mailer,[send_to])
            form.save()

            return fronts(request)

    return render(request,'volunteers/volunteerRegistration.html',{
        'form':form,
    })

def fronts(request):
    return HttpResponse('<h1>Registered</h1>')





