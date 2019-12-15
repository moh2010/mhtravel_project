from django.contrib import admin
from .models import Program, Category, Destination, City

#class ProgramAdmin(admin.ModelAdmin):
 #   list_display = ('',)

admin.site.register(Category)
admin.site.register(Destination)
admin.site.register(Program)
admin.site.register(City)
