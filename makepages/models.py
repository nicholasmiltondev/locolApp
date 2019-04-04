from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.

# Business Sear https://api.yelp.com/v3/businesses/search

class SearchTerm(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    term = models.CharField(max_length=500)

class NumberOfSearches(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    total = models.PositiveIntegerField(default=0)

class Favourites(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    favourite = models.CharField(max_length=500)