from .models import BasicInfoSection

def basic(request):
    basicInfo = BasicInfoSection.objects.all().first()
    return dict(basicInfo= basicInfo)