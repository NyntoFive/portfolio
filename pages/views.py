import random, os
from django.conf import settings
from django.http import JsonResponse, Http404
from django.shortcuts import render, reverse



def homepage(request, *args, **kwargs):
    context = os.path.join(settings.BASE_DIR, 'images')
    return render(request, "pages/home.html", {context:'django1.jpg'})

def aboutpage(request, *args, **kwargs):
    return render(request, "pages/draft.html")

def games(request, *args, **kwargs):
    return render(request, 'pages/breakout.html',{} )
