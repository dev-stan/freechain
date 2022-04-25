from urllib import request
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
import os



def home(request):
    return render(request, 'home.html')


def mainScirpt(request):

    from mysite.scripts import runJotaro
    runJotaro.runBot()

    return HttpResponse("""<html><script>window.location.replace('/');</script></html>""")

