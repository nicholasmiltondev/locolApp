from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.contrib.auth.models import User

# Create your views here.

class LoginView(TemplateView):
    template_name = 'login.html'

class SearchView(ListView):
    model = User
    template_name = "search.html"
    context_object_name = 'users'

    # def get_queryset(self):
    #
    #
    #
    #     return User.objects.filter(username__contains=self.kwargs['term'])

class ResultsView(TemplateView):
    template_name = "results.html"

class FavouritesView(TemplateView):
    template_name = "favourites.html"