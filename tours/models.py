from django.db import models
from django.urls import reverse
from smart_selects.db_fields import ChainedForeignKey

def program_directory_path(instance, filename):
     
    return '{0}_img/{1}'.format(instance.title, filename)

class Category(models.Model):
    title = models.CharField(max_length=200,db_index=True, null=True)
    slug = models.SlugField(max_length=200,unique=True, null=True)
    
    class Meta:
        ordering = ('title',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('tours:category_list', args=[self.slug])

class Destination(models.Model):
    title = models.CharField(max_length=200,db_index=True, null=True)
    slug = models.SlugField(max_length=200,unique=True, null=True)
    image_main= models.ImageField(upload_to=program_directory_path, blank=True, null=True)
    image_1 = models.ImageField(upload_to=program_directory_path, blank=True, null=True)
    image_2 = models.ImageField(upload_to=program_directory_path, blank=True, null=True)
    image_3 = models.ImageField(upload_to=program_directory_path, blank=True, null=True)
    description = models.TextField(null=True)
    available_front_page = models.BooleanField(default=True)
    class Meta:
        ordering = ('title',)
        verbose_name = 'destination'
        verbose_name_plural = 'destinations'
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('tours:program_list_by_destination', args=[self.slug])

class City(models.Model):
    destination = models.ForeignKey(Destination, related_name='des_city', on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=200, db_index=True, null=True)
    slug = models.SlugField(max_length=200, unique=True, null=True)
    description = models.TextField(null=True)

    class Meta:
        ordering = ('title',)
        verbose_name = 'city'
        verbose_name_plural = 'cities'

    def __str__(self):
        return self.title   

class Airline(models.Model):
    airline_name = models.CharField(max_length=200,db_index=True, null=True)
    airline_code =models.CharField(max_length=10, null=True)
    description = models.TextField(null=True)
    slug = models.SlugField(max_length=200,unique=True, null=True)
    
    class Meta:
        ordering = ('airline_code',)
        verbose_name = 'airline'
        verbose_name_plural = 'airlines'

    def __str__(self):
        return self.airline_name

    def get_absolute_url(self):
        return reverse('tours:airline_list', args=[self.slug])     

class Flight(models.Model):
    airline = models.ForeignKey(Airline, related_name='air_flight', on_delete=models.CASCADE, null=True)
    arrival_date = models.DateField(null=True)
    departure_date = models.DateField(null=True)
    slug = models.SlugField(max_length=200,unique=True, null=True)
    
    class Meta:
        ordering = ('arrival_date',)
        verbose_name = 'flight'
        verbose_name_plural = 'flights'

    def __str__(self):
        return self.slug

    def get_absolute_url(self):
        return reverse('tours:flight_list', args=[self.slug])               

class Hotel(models.Model):
    destination = models.ForeignKey(Destination, related_name='des_hotel', on_delete=models.CASCADE, null=True)
    city = models.ForeignKey(City, related_name='cit_hotel', on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=200,db_index=True, null=True)
    stars = models.IntegerField(null=True)
    slug = models.SlugField(max_length=200,unique=True, null=True)
    image_main = models.ImageField(upload_to=program_directory_path, blank=True, null=True)
    image_1 = models.ImageField(upload_to=program_directory_path, blank=True, null=True)
    image_2 = models.ImageField(upload_to=program_directory_path, blank=True, null=True)
    image_3 = models.ImageField(upload_to=program_directory_path, blank=True, null=True)
    description = models.TextField(null=True)
    available_front_page = models.BooleanField(default=True)
    class Meta:
        ordering = ('title',)
        verbose_name = 'hotel'
        verbose_name_plural = 'hotels'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('tours:hotel_list', args=[self.slug])        

class Program(models.Model):
    category = models.ForeignKey(Category, related_name='cat_programs', on_delete=models.CASCADE, null=True)
    destination = models.ForeignKey(Destination, related_name='des_programs', on_delete=models.CASCADE, null=True)
    city = ChainedForeignKey(
                City, 
                chained_field="destination",
                chained_model_field="destination",
                show_all=False,
                auto_choose=True,
                sort=True,
                related_name='cit_programs', 
                on_delete=models.CASCADE, 
                null=True)
    airline = models.ForeignKey(Airline, related_name='air_programs', on_delete=models.CASCADE, null=True)
    hotel_name = models.ForeignKey(Hotel, related_name='htl_programs', on_delete=models.CASCADE, null=True)
    flight = models.ForeignKey(Flight, related_name='fly_programs', on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=300, db_index=True, null=True)
    slug = models.SlugField(max_length=200, db_index=True, null=True)
    description = models.TextField(null=True)
    price_adt = models.DecimalField(max_digits=12, decimal_places=2, null=True)
    price_chd_one = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    price_chd_two = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    price_inf = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    district = models.CharField(max_length=200, null=True)
    image_main= models.ImageField(upload_to=program_directory_path, blank=True, null=True)
    image_1 = models.ImageField(upload_to=program_directory_path, blank=True, null=True)
    image_2 = models.ImageField(upload_to=program_directory_path, blank=True, null=True)
    image_3 = models.ImageField(upload_to=program_directory_path, blank=True, null=True)
    image_4 = models.ImageField(upload_to=program_directory_path, blank=True, null=True)
    image_5 = models.ImageField(upload_to=program_directory_path, blank=True, null=True)
    image_6 = models.ImageField(upload_to=program_directory_path, blank=True, null=True)
    available_front_page = models.BooleanField(default=True)
    available_programs_page = models.BooleanField(default=True)
    available_lastminut_page = models.BooleanField(default=True)
    available_tours_page = models.BooleanField(default=True)
    
    
    def __str__(self):
        return self.hotel_name.title 
        """ "+ self.title +" "+str(self.hotel_name.title)+" "+str(self.flight.arrival_date) " """

    def get_absolute_url(self):
            return reverse('tours:tour_detail', args=[self.id, self.slug])
                            

    class Meta:
        ordering = ('flight',)
        verbose_name = 'program'
        verbose_name_plural = 'programs' 
    





