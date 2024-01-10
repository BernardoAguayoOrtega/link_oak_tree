from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy

from .models import Link

# Create your views here.
class Links(ListView):
    model = Link
    template_name = 'link_oat/links.html'
    context_object_name = 'links'
    
class CreateLink(CreateView):
    model = Link
    fields = "__all__"
    template_name = 'link_oat/create_link.html'
    success_url = reverse_lazy('links')