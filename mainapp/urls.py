from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path('add_member', views.add_member, name="add_member"),
    path('printid', views.printid, name="printid"),
    path('gallery', views.gallery, name="gallery"),
    path('event', views.event, name="event"),
    path('about', views.about, name="about"),
    path('donate', views.donate, name="donate")
]

