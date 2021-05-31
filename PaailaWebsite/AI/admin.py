from django.contrib import admin
from .models import ArtificialIntellience, ServicesList
# Register your models here.


admin.site.register(ArtificialIntellience)

class ServicesListAdmin(admin.ModelAdmin):
    list_display = ('title','description')

admin.site.register(ServicesList, ServicesListAdmin)