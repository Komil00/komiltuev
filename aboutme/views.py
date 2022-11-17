from django.shortcuts import render

# Create your views here.
from django.views import generic

from aboutme.models import Otziv


class CreateOtzivView(generic.CreateView):
    model = Otziv
    template_name = 'home.html'
    fields = ['name', 'phone', 'address', 'email', 'message']
    success_url = '/'
