from django.db import models
from django.urls import reverse

class Category(models.Model):
    title = models.CharField(max_length=200,db_index=True)
    slug = models.SlugField(max_length=200,unique=True)
    
    class Meta:
        ordering = ('title',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.title


class Destination(models.Model):
    title = models.CharField(max_length=200,db_index=True)
    slug = models.SlugField(max_length=200,unique=True)

    class Meta:
        ordering = ('title',)
        verbose_name = 'destination'
        verbose_name_plural = 'destinations'
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('tours:program_list_by_destination', args=[self.slug])

class City(models.Model):
    title = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ('title',)
        verbose_name = 'city'
        verbose_name_plural = 'cities'

    def __str__(self):
        return self.title    

def program_directory_path(instance, filename):
     
    return '{0}_img/{1}'.format(instance.title, filename)

class Program(models.Model):
    category = models.ForeignKey(Category, related_name='cat_programs', on_delete=models.CASCADE)
    destination = models.ForeignKey(Destination, related_name='des_programs', on_delete=models.CASCADE)
    city = models.ForeignKey(City, related_name='cit_programs', on_delete=models.CASCADE)
    title = models.CharField(max_length=300, db_index=True)
    arrival_date = models.DateField()
    departure_date = models.DateField()
    description = models.TextField()
    price_adt = models.DecimalField(max_digits=12, decimal_places=2)
    price_chd_one = models.DecimalField(max_digits=10, decimal_places=2)
    price_chd_two = models.DecimalField(max_digits=10, decimal_places=2)
    price_inf = models.DecimalField(max_digits=10, decimal_places=2)
    hotel_name = models.CharField(max_length=200)
    district = models.CharField(max_length=200)
    stars = models.IntegerField()
    image_main= models.ImageField(upload_to=program_directory_path, blank=True)
    image_1 = models.ImageField(upload_to=program_directory_path, blank=True)
    image_2 = models.ImageField(upload_to=program_directory_path, blank=True)
    image_3 = models.ImageField(upload_to=program_directory_path, blank=True)
    image_4 = models.ImageField(upload_to=program_directory_path, blank=True)
    image_5 = models.ImageField(upload_to=program_directory_path, blank=True)
    image_6 = models.ImageField(upload_to=program_directory_path, blank=True)
    flight = models.CharField(max_length=50)
    flight_detail = models.TextField()
    available_front_page = models.BooleanField(default=True)
    available_programs_page = models.BooleanField(default=True)
    available_lastminut_page = models.BooleanField(default=True)
    available_tours_page = models.BooleanField(default=True)
    
    
    def __str__(self):
        return self.title +" "+self.hotel_name+" "+str(self.arrival_date) 

    def get_absolute_url(self):
            return reverse('tours:tour_detail', args=[self.id])
                            

    class Meta:
        ordering = ('arrival_date',)
        verbose_name = 'program'
        verbose_name_plural = 'programs' 
    





