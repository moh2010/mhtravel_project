from django.urls import path
from . import views 

app_name = 'tours'

urlpatterns = [
    path('', views.index, name='index'),
    path('<slug:category_slug>/', views.per_category, name='category_list'),
    path('about', views.about, name='about'),
    path('destination/<slug:des_slug>/', views.per_destination, name='program_list_by_destination'),
    path('packages', views.package, name='package'),
    path('<int:tour_id>/<slug:slug>/', views.tour_detail, name='tour_detail'),
    path('search', views.search, name='search'),
    path('contact', views.contact, name='contact'),

]