from django.shortcuts import render, HttpResponse, redirect
from modules.cause.models.cause_models import cause
from modules.cause.forms.cause_forms import causeForm


def index(request):
    form = causeForm()
    if (request.method == 'POST'):
        form = causeForm(request.POST)
        if (form.is_valid()):
            form.save()

            return fronts(request)

    return render(request, 'cause/Cause.html', {
        'form': form,
    })


def fronts(request):
    return HttpResponse('<h1>Cause registered</h1>')
