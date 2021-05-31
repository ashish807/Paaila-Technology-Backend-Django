from django.shortcuts import render
from .models import ArtificialIntellience, ServicesList
# Create your views here.


def ai(request):
    ai = ArtificialIntellience.objects.all().first()
    services = ServicesList.objects.all()

    context ={
        'ai':ai,
        'services':services,
    }
    return render(request, 'ai.html', context)