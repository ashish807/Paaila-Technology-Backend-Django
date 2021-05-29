from django.contrib import admin
from .models import NavFooter, FooterList, FooterListTitleContents,FollowUs
# Register your models here.


admin.site.register(NavFooter)

admin.site.register(FooterList)
admin.site.register(FollowUs)

class FooterListTitleContentsAdmin(admin.ModelAdmin):
    list_display =('footer', 'sub_Title')

admin.site.register(FooterListTitleContents, FooterListTitleContentsAdmin)