from django.shortcuts import get_object_or_404, render
# import the 404 as well
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
# choices at the same folder
from .choices import price_choices, state_choices, bedroom_choices
# load database into view
from .models import Listing

def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)
    paginator = Paginator(listings,3)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
    context = {
        'listings' : paged_listings
    }
    return render(request, 'listings/listings.html',context)


def listing(request,listing_id):
    # get an id or return 404
    listing = get_object_or_404(Listing, pk=listing_id) # get data by id from database
    context = {
        'listing': listing
    }
    return render(request, 'listings/listing.html',context)


def search(request):
    return render(request, 'listings/search.html')
