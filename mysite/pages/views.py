from django.shortcuts import render
from django.http import HttpResponse
# inmport dictionary for choices
# ↓↓↓↓↓ To call from listings.choices and import to pages/index.html
from listings.choices import price_choices, state_choices, bedroom_choices
# create a function for the index kink to urls API route
from listings.models import Listing
# Create a function for for the index link to
from realtors.models import Realtor


def index(request):
    # return HttpResponse("<h1>Hello</h1>")
    # show 3 listing pnly
    listings = Listing.objects.order_by(
        '-list_date').filter(is_published=True)[:3]
    # add choices into the objecct
    context = {
        'listings': listings,
        'state_choices': state_choices,
        'price_choices': price_choices,
        'bedroom_choices': bedroom_choices
    }
    return render(request, 'pages/index.html', context)


def about(request):
    # return HttpResponse("<h1>Hello</h1>")
    # get all realtors
    realtors = Realtor.objects.order_by('-hire_date')
    # get MVP, which is only one
    mvp_realtors = Realtor.objects.all().filter(is_mvp=True)
    context = {
        'realtors': realtors,
        'mvp_realtors': mvp_realtors
    }
    return render(request, 'pages/about.html', context)
