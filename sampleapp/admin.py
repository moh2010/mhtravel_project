from django.contrib import admin
from sampleapp.models import Airline, Flight, Ticket, Traveller


class FlightInline(admin.TabularInline):
    model = Flight
    extra = 1


class AirlineAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('airline_name',)}
    inlines = [
        FlightInline,
    ]


class TravellerInline(admin.TabularInline):
    model = Traveller
    extra = 0
    min_num = 1
    max_num = 9


class TicketAdmin(admin.ModelAdmin):
    inlines = [
        TravellerInline,
    ]


admin.site.register(Airline, AirlineAdmin)
admin.site.register(Ticket, TicketAdmin)
