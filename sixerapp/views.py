from django.shortcuts import render, redirect
from .models import Gig, Profile
from django.contrib.auth.decorators import login_required
from .forms import GigForm

# Create your views here.

def home(request):
    gigs = Gig.objects.filter(status=True)
    return render(request, 'home.html', {"gigs": gigs})

def gig_detail(request, id):
    try:
        gig = Gig.objects.get(id=id)
    except Gig.DoesNotExist:
        return redirect('/')
    return render(request, 'gig_detail.html', {'gig': gig})


def edit_gig(request, id):
    try:
        gig = Gig.objects.get(id=id, user=request.user)
        error = ""
        if request.method == 'POST':
            gig_form = GigForm(request.POST, request.FILES, instance=gig)
            if gig_form.is_valid():
                gig.save()
                return redirect('my_gigs')
            else:
                error: 'Data is not valid. Something went wrong!'

        return render(request, 'edit_gig.html', {'gig': gig, 'error': error})
    except Gig.DoesNotExist:
        return redirect('/')

@login_required(login_url="/")
def create_gig(request):
    error = ''
    if request.method == 'POST':
        gig_form = GigForm(request.POST, request.FILES)
        if gig_form.is_valid():
            gig = gig_form.save(commit=False)
            gig.user = request.user
            gig.save()
            return redirect ('my_gigs')
        else:
            print(gig_form.errors)
            error = 'Data is not valid'

    gig_form = GigForm()
    return render(request, 'create_gig.html', {'gig_form': gig_form, "error": error})

@login_required(login_url="/")
def my_gigs(request):
    gigs = Gig.objects.filter(user=request.user)
    return render(request, 'my_gigs.html', {'gigs': gigs})


@login_required(login_url="/")
def profile(request, username):
    try:
        profile = Profile.objects.get(user__username=username)
    except Profile.DoesNotExist:
        redirect('/')
        
    gigs = Gig.objects.filter(user=profile.user, status=True)
    return render(request, 'profile.html', { 'gigs': gigs, 'profile': profile})
