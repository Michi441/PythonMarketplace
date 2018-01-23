from django.shortcuts import render
from .models import Gig

# Create your views here.

def home(request):
    gigs = Gig.objects.filter(status=True)
    return render(request, 'home.html', {"gigs": gigs})

def gig_detail(request, id):
    return render(request, 'gig_detail.html', {})
