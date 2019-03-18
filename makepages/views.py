from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.

class LoginView(TemplateView):
    template_name = 'login.html'

class SearchView(TemplateView):
    template_name = "search.html"

class ResultsView(TemplateView):
    template_name = "results.html"

class FavouritesView(TemplateView):
    template_name = "favourites.html"