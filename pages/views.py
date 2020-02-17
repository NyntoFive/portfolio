import random
from django.conf import settings
from django.http import JsonResponse, Http404
from django.shortcuts import render, reverse



def homepage(request, *args, **kwargs):
    return render(request, "pages/home.html")

def aboutpage(request, *args, **kwargs):
    return render(request, "pages/draft.html")

def games(request, *args, **kwargs):
    return render(request, 'pages/breakout.html',{} )
