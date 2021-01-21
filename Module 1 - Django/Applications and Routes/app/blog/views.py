from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    """
    Homepage
    """
    return HttpResponse('<h1>Blog Home </h1>')

def about(request):
    """
    about page
    """
    return HttpResponse('<h1>Blog About </h1>')
