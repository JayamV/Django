from django.shortcuts import render,redirect
from django.http import HttpResponse

def index(request):
    return HttpResponse("hello guys")

def detail(request, post_id):
    return HttpResponse(f"detail page for post {post_id}")

def jayam(request):
    return HttpResponse("<html><body><h1>JAYAM</h1></body></html>")

def old_link(request):
    return redirect(new_link)

def new_link(request):
    return HttpResponse("This is the new link destination.")