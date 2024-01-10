from django.urls import path

from . import views

urlpatterns = [
    path('', views.Links.as_view() , name='links' ),
]