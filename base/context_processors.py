from .models import *
from django.db.models import Q
def base_data(request):
    social_medias=SocialMedia.objects.all()
    facts=FunFact.objects.all()
    main_info=Main.objects.last()
    images=BackgroundImage.objects.last()
    partners=Partner.objects.all()
    return  {'social_medias':social_medias, 'partners':partners,'images':images,
         'facts':facts, 'main_info':main_info}