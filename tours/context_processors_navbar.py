from .models import Destination, Category

def navbar_index(request, category_slug=None):
    navbar_destinations = Destination.objects.all()
    navbar_categories = Category.objects.all()
    
    return {
       'navbar_destinations':navbar_destinations,
       'navbar_categories':navbar_categories      
    }
    
  