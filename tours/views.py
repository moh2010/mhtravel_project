from django.shortcuts import render, get_object_or_404
from .models import Program, Category, Destination, City, Flight
from django.core.paginator import EmptyPage, Paginator, PageNotAnInteger
from .choices import persons_choices

""" def index(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    programs = Program.objects.order_by('arrival_date').filter(available_front_page=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        programs = programs.filter(category=category) 
    destinations = Destination.objects.all()
    paginator = Paginator(programs, 3)
    page = request.GET.get('page')
    paged_programs = paginator.get_page(page)
    context = {
       'category': category,
       'categories':categories,
       'programs': paged_programs,
       'destinations': destinations,
       'persons_choices': persons_choices
    }
    return render(request, 'tours/index.html', context) """

def index(request, category_slug=None):
    programs = Program.objects.order_by('flight__arrival_date').filter(available_front_page=True)[:3]
    destinations = Destination.objects.all()
    categories = Category.objects.all()   
    context = {
       'programs': programs,
       'destinations':destinations,
       'categories':categories
    }
    return render(request, 'tours/index.html', context)

def about(request):
    return render(request, 'tours/about.html')

def per_category(request, category_slug=None):
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        programq = Program.objects.filter(category=category)
        context = {
        'category': category ,
        'programq': programq
        }    
    return render (request, 'tours/hotels.html', context)

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


def tour_detail(request, tour_id, slug):
    tour = get_object_or_404(Program, id=tour_id, slug=slug, available_programs_page=True)
    context = {
       'tour': tour
    }
    return render (request, 'tours/tour_details.html', context)    

def search(request):
    queryset_list = Program.objects.order_by('arrival_date')
    destinations  = Destination.objects.all()
   
    # destination  
    if 'land' in request.GET:
        land = request.GET['land']
        if land :
            queryset_list = queryset_list.filter(destination__title__iexact=land)

    # arrival Date
    if 'arrival_date' in request.GET:
        arrival_date = request.GET['arrival_date']
        if arrival_date :
            queryset_list = queryset_list.filter(arrival_date__lte=arrival_date)        
    context = {
       'programs': queryset_list,
       'destinations': destinations,
       'persons_choices': persons_choices
       
    }
    return render(request, 'tours/index.html', context)


def contact(request):
    return render (request, 'tours/contact.html')
