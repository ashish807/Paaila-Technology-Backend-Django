from django.contrib import admin
from .models import ICareerSection, IIIWoringWithUs, IICurrentOpeningPosition, IVWorkingWithUsContent, ResumeSection
# Register your models here.

admin.site.register(ICareerSection)


class IICurrentOpeningPositionAdmin(admin.ModelAdmin):
    list_display = ('position', 'location', 'title','Deadline','is_available')
    list_filter =('position','title','is_available')
    list_editable=('is_available',)

admin.site.register(IICurrentOpeningPosition, IICurrentOpeningPositionAdmin)




class IVWorkingWithUsContentInline(admin.TabularInline):
    model = IVWorkingWithUsContent
    extra=0


class IIIWoringWithUsAdmin(admin.ModelAdmin):
    list_display =('title', 'title_id')
    inlines =[IVWorkingWithUsContentInline]

admin.site.register(IIIWoringWithUs,IIIWoringWithUsAdmin)


class ResumeSectionAdmin(admin.ModelAdmin):
    list_display =('full_name', 'email', 'address', 'phone')
    list_filter = ('full_name','email')
    search_fields =('full_name','email','phone')

admin.site.register(ResumeSection,ResumeSectionAdmin)