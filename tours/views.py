from django.shortcuts import render, get_object_or_404
from .models import Program, Category, Destination, City
from django.core.paginator import EmptyPage, Paginator, PageNotAnInteger
from .choices import persons_choices

def index(request):
    programs = Program.objects.order_by('arrival_date').filter(available_front_page=True)
    destinations = Destination.objects.all()
    paginator = Paginator(programs, 4)
    page = request.GET.get('page')
    paged_programs = paginator.get_page(page)
    context = {
       'programs': paged_programs ,
       'destinations': destinations,
       'persons_choices': persons_choices
    }
    return render(request, 'tours/index.html', context)

def about(request):
    return render(request, 'tours/about.html')

def destination(request):
    return render (request, 'tours/destination.html')

def per_destination(request, des_slug=None):
    if des_slug:
        destination = get_object_or_404(Destination, slug=des_slug)
        program = Program.objects.filter(destination=destination)
        context = {
        'destination': destination ,
        'program': program
        }    
    return render (request, 'tours/per_destination.html', context)

def package(request):
    programz = Program.objects.order_by('arrival_date').filter(available_programs_page=True)
    destinations = Destination.objects.all()
    context = {
       'programz': programz ,
       'destinations': destinations
    }
    return render (request, 'tours/packages.html', context)

def tour_detail(request, tour_id):
    tour = get_object_or_404(Program, id=tour_id)
    context = {
       'tour': tour
    }
    return render (request, 'tours/tour_details.html', context)    

def search(request):
    queryset_list = Program.objects.order_by('arrival_date')
    destinations  = Destination.objects.all()
   
    if 'land' in request.GET:
        land = request.GET['land']
        if land :
            queryset_list = queryset_list.filter(destination__title__iexact=land)
    context = {
       'programs': queryset_list,
       'destinations': destinations,
       'persons_choices': persons_choices
       
    }
    return render(request, 'tours/search.html', context)



def contact(request):
    return render (request, 'tours/contact.html')
