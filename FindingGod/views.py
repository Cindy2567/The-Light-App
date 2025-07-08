#from django.http import HttpResponse
from django .shortcuts import render
from Christ.models import Devotional


def homepage(request):
   # return HttpResponse("Welcome to the Light App page.")
   return render(request, 'home.html')

def sermon(request):
   # return HttpResponse("Welcome to the Sermons  page.")
   return render(request, 'sermons.html')

def events(request):
    devotionals = Devotional.objects.order_by('-date')[:5]
    return render(request, 'events.html', {'devotionals': devotionals})



def devotional_list(request):
    devotionals = Devotional.objects.order_by('-date')[:5]  # Show latest 5
    return render(request, 'devotionals/list.html', {'devotionals': devotionals})



