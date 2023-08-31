from django.shortcuts import render, HttpResponse
from.models import MusicItem
from.models import TourItem
from django.contrib.auth.decorators import login_required

# Create your views here.
# The Home veiw renders the home template. 
def home(request):
    return render(request, "home.html")

# The music veiw renders the template with a database of the bands music and renders each item using a dictionary. 
def music(request):
    items = MusicItem.objects.all()
    return render(request, "music.html", {"music": items })

# Login required decorator user to prevent access to users that are not logged in from veiwing the tours page.
# The tours veiw renders the tour template with a database of the tour information and renders each tour using a dictionary. 
@login_required(login_url='/user_auth/login/')
def tours(request):
    place = TourItem.objects.all()
    return render(request, "tour.html", {"tour": place})