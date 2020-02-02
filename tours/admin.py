from django.contrib import admin
from .models import Program, Category, Destination, City, Hotel, Airline, Flight

class ProgramAdmin(admin.ModelAdmin):
    list_display = ('id','title','price_adt','category','available_front_page','available_programs_page','available_lastminut_page','available_tours_page')
    list_display_links = ('id','title','price_adt')
    list_filter = ('flight',)
    list_editable = ('available_front_page','available_programs_page','available_lastminut_page','available_tours_page')
    search_fields = ('title','description','destination','city','district',)

admin.site.register(Category)
admin.site.register(Destination)
admin.site.register(Program, ProgramAdmin)
admin.site.register(City)
admin.site.register(Hotel)
admin.site.register(Airline)
admin.site.register(Flight)
