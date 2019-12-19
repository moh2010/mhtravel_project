from django.shortcuts import render, get_object_or_404
from .models import Program, Category, Destination, City


def index(request):
    programs = Program.objects.all()
    destinations = Destination.objects.all()
    context = {
       'programs': programs ,
       'destinations': destinations
    }
    return render(request, 'tours/index.html', context)

def about(request):
    return render(request, 'tours/about.html')

def destination(request):
    return render (request, 'tours/destination.html')

def package(request):
    return render (request, 'tours/packages.html')

def tour_detail(request, id):
    tour = get_object_or_404(Program, id=id)
    context = {
       'tour': tour
    }
    return render (request, 'tours/tour_details.html', context)    

def search(request):
    return render (request, 'tours/search.html')


def contact(request):
    return render (request, 'tours/contact.html')
