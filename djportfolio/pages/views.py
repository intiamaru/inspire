from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# Create your views here.
def home_view(request, *args, **kwargs): # *args, **kwargs
    return render(request, "pages/home.html", {})

def contact_view(request, *args, **kwargs):
    return render(request, "pages/contact.html", {})
