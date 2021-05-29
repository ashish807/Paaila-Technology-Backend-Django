from .models import NavFooter, FooterListTitleContents, FooterList, FollowUs
from datetime import datetime

def nav_content(request):
    currentYear = datetime.now().year
    navFooter = NavFooter.objects.all().first()
    footer_list = FooterList.objects.all()
    footer_list_content = FooterListTitleContents.objects.all()
    follow = FollowUs.objects.all()

    return dict(navFooter=navFooter, footer_list=footer_list, footer_list_content=footer_list_content, follow=follow,currentYear=currentYear)