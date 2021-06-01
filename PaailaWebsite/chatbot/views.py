from django.shortcuts import render
from .models import ISlidingScreenShotImage, IIAdvertising,IIICustomerUsingOurChatBot,IVSecondAdvertising
# Create your views here.


def chatbot(request):
    slidings = ISlidingScreenShotImage.objects.all()
    advertisement1 = IIAdvertising.objects.all()
    clients = IIICustomerUsingOurChatBot.objects.all()
    client = IIICustomerUsingOurChatBot.objects.all().first()
    last_ad = IVSecondAdvertising.objects.all().first()
    context ={
        'slidings':slidings,
        'advertisement1':advertisement1,
        'clients':clients,
        'client':client,
        'last_ad':last_ad,
    }
    return render(request,'chatbot.html', context)