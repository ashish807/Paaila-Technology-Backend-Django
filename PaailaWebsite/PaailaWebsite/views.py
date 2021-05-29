
from django.shortcuts import render
from homepage.models import ISlidingImage, IIQuantityTitle, IIIApplicationArea, IVMediaCoverage, VCompaniesLoveList
def home(request):
    sliding_image = ISlidingImage.objects.all()
    quantities = IIQuantityTitle.objects.all()
    applications = IIIApplicationArea.objects.all()
    heading_application = IIIApplicationArea.objects.all().first()
    medias = IVMediaCoverage.objects.all()
    title_media =  IVMediaCoverage.objects.all().first()
    companies = VCompaniesLoveList.objects.all()
    company_name = VCompaniesLoveList.objects.all().first()

    context = {
        'sliding_image':sliding_image,
        'quantities':quantities,
        'applications':applications,
        'medias':medias,
        'companies':companies,
        'heading_application':heading_application,
        'title_media': title_media,
        'company_name':company_name,
    }
    return render(request, 'home.html', context)