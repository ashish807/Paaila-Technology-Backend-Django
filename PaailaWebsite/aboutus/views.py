from django.shortcuts import render
from .models import IAboutUSSection, IIAboutTextImageAlterSection, IIICompanyProgress, IVWorkingSteps, VTeamBox, VISubscribe

# Create your views here.

def about(request):
    about= IAboutUSSection.objects.all().first()
    about_text_images = IIAboutTextImageAlterSection.objects.all()
    progresses = IIICompanyProgress.objects.all()
    progress = IIICompanyProgress.objects.all().first()

    working_steps = IVWorkingSteps.objects.all()
    working_step = IVWorkingSteps.objects.all().first()
    teams = VTeamBox.objects.all()
    team = VTeamBox.objects.all().first()
    subscribe = VISubscribe.objects.all().first()
    context ={
        'about':about,
        'about_text_images':about_text_images,
        'progresses':progresses,
        'progress':progress,
        'working_steps':working_steps,
        'working_step':working_step,
        'teams':teams,
        'team':team,
        'subscribe':subscribe,
    }
    return render(request, 'aboutus.html', context)