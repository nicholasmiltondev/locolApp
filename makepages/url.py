from django.contrib import admin
from django.urls import path
from .views import *
from django.urls import path, include

urlpatterns = [

    path('', include('django.contrib.auth.urls')),
    path('search/', SearchView.as_view(), name="search"),
    path('search/<term>', SearchView.as_view(), name="search_user"),
    path('results/', ResultsView.as_view(), name="results"),
    path('results/<term>', ResultsView.as_view(), name="results"),
    path('favourites/', FavouritesView.as_view(), name="favourites"),
]
