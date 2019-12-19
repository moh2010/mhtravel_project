from django.contrib import admin
from .models import Program, Category, Destination, City

class ProgramAdmin(admin.ModelAdmin):
    list_display = ('id','title','arrival_date','departure_date','price_adt','flight','category','available_front_page','available_programs_page','available_lastminut_page','available_tours_page')
    list_display_links = ('id','title','arrival_date','price_adt')
    list_filter = ('arrival_date',)
    list_editable = ('available_front_page','available_programs_page','available_lastminut_page','available_tours_page')
    search_fields = ('title','description','destination','city','district','flight','hotel_name')

admin.site.register(Category)
admin.site.register(Destination)
admin.site.register(Program, ProgramAdmin)
admin.site.register(City)
