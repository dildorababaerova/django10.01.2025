from django.shortcuts import render
from .models import Homepage

def index(request):
    homepage_data = Homepage.objects.order_by("-date")[:5]
    return render(request, 'maalaus/homepage.html', {'homepage_data': homepage_data})
