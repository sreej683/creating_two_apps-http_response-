from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def srujana(request):
    return HttpResponse('<h1><marquee>Srujana thinnava ra</marquee></h1>')


def lasya(request):
    return HttpResponse('<h1><marquee>Lasya is good girl</marquee></h1>')
