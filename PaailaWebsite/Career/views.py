from django.shortcuts import render, redirect, get_object_or_404
from .models import ICareerSection, IIIWoringWithUs, IICurrentOpeningPosition, IVWorkingWithUsContent, ResumeSection

from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.contrib import messages, auth
from .forms import UploadForm
import os
from pathlib import Path

# Create your views here.

def career(request):
   
# Build paths inside the project like this: BASE_DIR / 'subdir'.
    BASE_DIR = Path(__file__).resolve().parent.parent
    print(BASE_DIR)
    career = ICareerSection.objects.all().first()
    openings = IICurrentOpeningPosition.objects.filter(is_available=True)
    works = IIIWoringWithUs.objects.all()
    work_head = IIIWoringWithUs.objects.all().first()
    work_contents = IVWorkingWithUsContent.objects.all()
    work_content_first = IVWorkingWithUsContent.objects.all().first()

    context ={
        'career':career,
        'openings':openings,
        'works':works,
        'work_contents':work_contents,
        'work_head':work_head,
        'work_content_first':work_content_first,

    }

    if request.method == "POST":
 
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid:
            data = ResumeSection()
            
            data.full_name = request.POST['full_name']
            data.email = request.POST['email']
            data.address = request.POST['address']
            data.phone = request.POST['phone']
            data.resume = request.FILES['resume']
            data.position = request.POST['position']
            data.title = request.POST['title']
            data.strength = request.POST['strength']
            data.save()

            # ResumeSection.objects.create(**request.POST)

            mail_subject = 'Thank you for applying'
            message = render_to_string('includes/email_send.html', {
                        'name': request.POST['full_name'],

                    })
            to_email = request.POST['email']
            send_email = EmailMessage(mail_subject, message, to=[to_email])
            send_email.send()

            messages.success(request, 'Thank you for applying')

            return redirect('career')
        else:
            messages.success(request, 'Invalid Form')

            return redirect('career')


            


    
    return render(request, 'career.html', context)