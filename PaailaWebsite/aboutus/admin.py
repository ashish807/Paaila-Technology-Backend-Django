from django.contrib import admin
from .models import IAboutUSSection, IIAboutTextImageAlterSection, IIICompanyProgress, IVWorkingSteps,VTeamBox ,VISubscribe
# Register your models here.


admin.site.register(IAboutUSSection)

class IIAboutTextImageAlterSectionAdmin(admin.ModelAdmin):
    list_display=('title','push_image_to_left')

admin.site.register(IIAboutTextImageAlterSection, IIAboutTextImageAlterSectionAdmin)


class IIICompanyProgressAdmin(admin.ModelAdmin):
    list_display =('title','percentage_progress')

admin.site.register(IIICompanyProgress, IIICompanyProgressAdmin)


admin.site.register(IVWorkingSteps)

class VTeamBoxAdmin(admin.ModelAdmin):
    list_display = ('name','designation')

admin.site.register(VTeamBox, VTeamBoxAdmin)

admin.site.register(VISubscribe)