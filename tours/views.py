from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'tours/index.html')

def about(request):
    return render(request, 'tours/about.html')

def destination(request):
    return render (request, 'tours/destination.html')

def package(request):
    return render (request, 'tours/packages.html')

def tour_detail(request):
    return render (request, 'tours/tour_details.html')    

def search(request):
    return render (request, 'tours/search.html')


def contact(request):
    return render (request, 'tours/contact.html')
