from django.shortcuts import render, redirect
from .models import ContactUsSection, BasicInfoSection
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.contrib import messages, auth
# Create your views here.

def contact(request):
    contacts = ContactUsSection.objects.all().first()
    context ={
        'contact':contacts,
    }
    return render(request, 'contact.html', context)

def send_email(request):
    if request.method=='POST':
        name = request.POST['name']
        surname = request.POST['surname']
        
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        full_name = name + " " + surname
        basic = BasicInfoSection.objects.all().first()
        mail_subject = 'Enquiry Email'
        message = render_to_string('includes/send_email.html', {
               'name':full_name,
               
               'email':email,
               'phone':phone,
               'message':message,
                
            })
        to_email = basic.email
        send_E = EmailMessage(mail_subject, message, to=[to_email])
        send_E.send()
        messages.success(request, 'Thanks You, we will contact you soon')
        return redirect('contact')


