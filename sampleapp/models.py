from django.db import models
from django.utils import timezone


class Airline(models.Model):
    airline_name = models.CharField(max_length=200, db_index=True)
    airline_code = models.CharField(max_length=10)
    description = models.TextField(blank=True, null=True)
    slug = models.SlugField(max_length=200, unique=True)

    def __str__(self):
        return self.airline_name


class Flight(models.Model):
    airline = models.ForeignKey(Airline, related_name='airline_flight', on_delete=models.CASCADE)
    flight_model = models.CharField(max_length=60, blank=True, null=True)
    from_location = models.CharField(max_length=60, blank=False, null=False)
    to_location = models.CharField(max_length=60, blank=False, null=False)
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    available_seats = models.IntegerField()

    def __str__(self):
        return str(self.flight_model)


class Ticket(models.Model):
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE, related_name='flight_ticket')
    booking_date = models.DateTimeField(default=timezone.now)
    # number_of_traveller = models.IntegerField()

    def __str__(self):
        return str(self.flight)


class Traveller(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female')
    ]

    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE, related_name='traveller_ticket')
    firstname = models.CharField(max_length=60, blank=False, null=False)
    lastname = models.CharField(max_length=60, blank=False, null=False)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='M')
    age = models.IntegerField(blank=False, null=False)
    email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return ''.format(self.firstname + ' ' + self.firstname)
