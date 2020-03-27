from django.shortcuts import render, redirect
from .models import *

# Create your views here.
def index(request):
    matches = Match.objects.all()
    context = {
        'matches' : matches,
    }
    return render(request, 'index.html',context)