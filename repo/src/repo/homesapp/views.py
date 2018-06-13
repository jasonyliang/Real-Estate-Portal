from django.shortcuts import render

from django.views import generic 
from .models import Location, Property
# Create your views here.

class IndexView(generic.ListView):
    template_name = 'index.html'

    def get_queryset(self):
        return Location.objects.all()
    
class LocationView(generic.DetailView):
    model = Location
    template_name = "locationview.html"



class PropertyView(generic.DeleteView):
    model = Property
    template_name = "propertyview.html"
