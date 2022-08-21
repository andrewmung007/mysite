from django.contrib import admin
from .models import Listing

# Register your models here.


class ListingAdmin(admin.ModelAdmin):
    
    # report format 
    list_display = ('id', 'title', 'is_published',
                    'price', 'list_date', 'realtor')
    
    # click to request record for review in the report
    list_display_links = ('id', 'title')
    
    
    list_filter = ('realtor',)
    
    list_editable = ('is_published',)
    
    search_fields = ('title', 'desciption', 'address',
                     'city', 'state', 'zipcode', 'price')
    
    list_per_page = 25


admin.site.register(Listing, ListingAdmin)
