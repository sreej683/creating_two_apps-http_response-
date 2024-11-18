from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def lasya(request):
    return HttpResponse('<h1><marquee>lasya how are u??</marquee></h1>')