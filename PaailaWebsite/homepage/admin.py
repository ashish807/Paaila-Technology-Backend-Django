from django.contrib import admin
from .models import ISlidingImage, IIQuantityTitle, IIIApplicationArea, IVMediaCoverage, VCompaniesLoveList
# Register your models here.

class ISlidingImageAdmin(admin.ModelAdmin):
    list_display = ('heading', 'description')
admin.site.register(ISlidingImage, ISlidingImageAdmin)

class IIQuantityTitleAdmin(admin.ModelAdmin):
    list_display = ('title', 'quantity')
admin.site.register(IIQuantityTitle, IIQuantityTitleAdmin)


class IIIApplicationAreaAdmin(admin.ModelAdmin):
    list_display = ('description',)
admin.site.register(IIIApplicationArea, IIIApplicationAreaAdmin)

class IVMediaCoverageAdmin(admin.ModelAdmin):
    list_display = ('media_name','heading')
admin.site.register(IVMediaCoverage, IVMediaCoverageAdmin)


class VCompaniesLoveListAdmin(admin.ModelAdmin):
    list_display =('company_name',)

admin.site.register(VCompaniesLoveList,VCompaniesLoveListAdmin)