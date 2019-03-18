from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', LoginView.as_view(), name='index'),
    path('search/', SearchView.as_view(), name="search"),
    path('results/', ResultsView.as_view(), name="results"),
    path('favourites/', FavouritesView.as_view(), name="favourites")
]
