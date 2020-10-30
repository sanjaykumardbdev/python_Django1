from django.shortcuts import render


# Create your views here.
# from django_projects.project_1.travello.models import Destination
from .models import Destination


def index(request):
    # return HttpResponse("<h1>Hello World</h1>")



    # dest1 = Destination()
    # dest1.name = 'Mumbai'
    # dest1.price = 111
    # dest1.img = '1.png'
    # dest1.desc = 'City That Never Sleeps'
    # dest1.offer = False
    # dest1.days = 3
    #
    # dest2 = Destination()
    # dest2.name = 'Bangalore'
    # dest2.price = 7999
    # dest2.img = '2.png'
    # dest2.desc = 'Software City'
    # dest2.offer = True
    # dest2.days = 5
    #
    # dest3 = Destination()
    # dest3.name = 'Hydrabad'
    # dest3.price = 8999
    # dest3.img = '3.png'
    # dest3.desc = 'Software City 2'
    # dest3.offer = True
    # dest3.days = 7

    # dests = [dest1, dest2, dest3]
    # return render(request, 'travel_destination.html', {'price': 750})

    dests = Destination.objects.all()
    return render(request, 'travel_destination.html', {'dests': dests})


