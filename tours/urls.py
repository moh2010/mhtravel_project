from django.urls import path
from . import views 

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('destination', views.destination, name='destination'),
    path('packages', views.package, name='package'),
    path('<int:program_id>', views.tour_detail, name='tour_detail'),
    path('search', views.search, name='search'),
    path('contact', views.contact, name='contact'),

]