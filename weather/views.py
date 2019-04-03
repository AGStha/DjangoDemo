from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def kathmandu(request):
    return HttpResponse("This is kathmandu weather")
def pokhara(request):
    return HttpResponse("This is pokharas weather")
def index(request):
    return HttpResponse("This is inde page of weather")
