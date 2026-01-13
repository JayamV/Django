from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("hello guys")


def detail(request):
    return HttpResponse("detail page")