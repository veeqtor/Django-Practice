from django.shortcuts import render
from listings.models import Listing
from listings.choices import BEDROOM_CHOICE, PRICE_CHOICE, STATE_CHOICE


from realtors.models import Realtor


def index(request):
    listings = Listing.objects.order_by(
        'list_date').filter(is_published=True)[:3]
    context = {
        'listings': listings,
        'state_choices': STATE_CHOICE,
        'bedroom_choices': BEDROOM_CHOICE,
        'price_choices': PRICE_CHOICE,
    }
    return render(request, 'pages/index.html', context)


def about(request):

    # realtors
    realtors = Realtor.objects.order_by('-hire_date')

    # get mvp
    mvp_realtors = Realtor.objects.all().filter(is_mvp=True)

    context = {
        'realtors': realtors,
        'mvp_realtors': mvp_realtors,
    }

    return render(request, 'pages/about.html', context)
