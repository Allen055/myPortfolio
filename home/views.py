from django.shortcuts import render
from .models import Home

# Create your views here.

def index(request):

    home = Home.objects.first()

    context = {
        'home': home,
    }

    return render(
        request,
        'home/index.html',
        context
    )