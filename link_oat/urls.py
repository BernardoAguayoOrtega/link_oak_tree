from django.urls import path

from . import views

urlpatterns = [
    path('', views.Links.as_view() , name='links' ),
    path("link/create", views.CreateLink.as_view(), name="create_link"),
]