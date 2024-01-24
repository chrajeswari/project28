from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from app.forms import *
from app.models import *

def insert_topic(request):
    ETFO=Topicform()
    d={'ETFO':ETFO}
    if request.method=='POST':
        TFDO=Topicform(request.POST)
        if TFDO.is_valid():
            TFDO.save()
            return HttpResponse('data inserted')
    return render(request,'insert_topic.html',d)

def insert_webpage(request):
    EWFO=Webpageform()
    d={'EWFO':EWFO}
    if request.method=='POST':
        WFDO=Webpageform(request.POST)
        if WFDO.is_valid():
            WFDO.save()
            return HttpResponse('data inserted')
    return render(request,'insert_webpage.html',d)

def insert_access(request):
    EAFO=AccessRecordform()
    d={'EAFO':EAFO}
    if request.method=='POST':
        AFDO=AccessRecordform(request.POST)
        if AFDO.is_valid():
            AFDO.save()
            return HttpResponse('data inserted')
    return render(request,'insert_access.html',d)

