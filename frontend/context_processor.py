from backend.models import Setting,AboutMe,SocialSite

def Common(request):
    context={
        'setting':Setting.objects.first(),
        'aboutme':AboutMe.objects.first(),
        'socialsites':SocialSite.objects.all()
    }
    return context