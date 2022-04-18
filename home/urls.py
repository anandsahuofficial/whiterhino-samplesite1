from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
     path("", views.index, name='home'),
     path("pritam", views.pritam, name='pritam'),
#      path("group", views.group, name='group'),
     path("team", views.team, name='team'),
     path("research", views.research, name='research'),
    
     path("services", views.services, name='services'),
     path("contact", views.contact, name='contact'),
     path("pritam2", views.pritam2, name='pritam2'),
     path("book", views.book, name='book'),
     path("patent", views.patent, name='patent'),
     path("reviews", views.reviews, name='reviews'),
     
     path("researchpaper", views.researchpaper, name='researchpaper'),
     path("Research_overview", views.Research_overview, name='Research_overview'),
     path("researchA", views.researchA, name='researchA'),
     path("researchB", views.researchB, name='researchB'),
     path("researchC", views.researchC, name='researchC'),
     path("researchD", views.researchD, name='researchD'),
     path("researchE", views.researchE, name='researchE'),
     path("researchF", views.researchF, name='researchF'),
     path("researchG", views.researchG, name='researchG'),

     path("coverpages", views.coverpages, name='coverpages'),
      path("gallery", views.gallery, name='gallery'),
      path("labtour", views.labtour, name='labtour'),     
]
