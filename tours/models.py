from django.db import models

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

class City(models.Model):
    title = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ('title',)
        verbose_name = 'city'
        verbose_name_plural = 'cities'

    def __str__(self):
        return self.title    

class Program(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE )
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    title = models.CharField(max_length=300, db_index=True)
    arrival_date = models.DateField()
    departure_date = models.DateField()
    description = models.TextField()
    price_adt = models.DecimalField(max_digits=6, decimal_places=2)
    price_chd = models.DecimalField(max_digits=6, decimal_places=2)
    price_inf = models.DecimalField(max_digits=6, decimal_places=2)
    hotel_name = models.CharField(max_length=200)
    disrict = models.CharField(max_length=200)
    stars = models.IntegerField()
    image_main= models.ImageField()
    image_1 = models.ImageField()
    image_2 = models.ImageField()
    image_3 = models.ImageField()
    image_4 = models.ImageField()
    image_5 = models.ImageField()
    image_6 = models.ImageField()
    flight = models.CharField(max_length=50)
    flight_detail = models.TextField()
    available_front_page = models.BooleanField(default=True)
    available_programs_page = models.BooleanField(default=True)
    available_lastminut_page = models.BooleanField(default=True)
    available_tours_page = models.BooleanField(default=True)

    
    def __str__(self):
        return self.title 

    class Meta:
        ordering = ('arrival_date',)
        verbose_name = 'program'
        verbose_name_plural = 'programs' 
    




