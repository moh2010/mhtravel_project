from django.contrib import admin
from .models import Program, Category, Destination, City, Hotel, Airline, Flight


class ProgramAdmin(admin.ModelAdmin):
    list_display = ('id','title','price_adt','category','flight_date','available_front_page','available_programs_page','available_lastminut_page','available_tours_page')
    model = Program
    list_display_links = ('id','title','price_adt','flight_date')
    list_filter = ('flight',)
    list_editable = ('available_front_page','available_programs_page','available_lastminut_page','available_tours_page')
    search_fields = ('title','description','destination','city','district',)

    def flight_date(self, obj):
        return obj.flight.arrival_date


admin.site.register(Category)
admin.site.register(Destination)
admin.site.register(Program, ProgramAdmin)
admin.site.register(City)
admin.site.register(Hotel)
admin.site.register(Airline)
admin.site.register(Flight)
