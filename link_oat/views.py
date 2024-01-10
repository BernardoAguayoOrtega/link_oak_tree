from django.shortcuts import render
from django.views.generic.list import ListView

from .models import Link

# Create your views here.
class Links(ListView):
    model = Link
    template_name = 'link_oat/links.html'
    context_object_name = 'links'