from django.shortcuts import render
from app.models import *
# Create your views here.
def display_topic(request):
    LTO=Topic.objects.all()
    d={'LTO':LTO}
    return render(request,'display_topic.html',d)

def display_Webpages(request):
    LTO=Topic.objects.all()
    d={'LTO':LTO}
    return render(request,'display_Webpages.html',d)    
