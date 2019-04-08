from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.

# Business Sear https://api.yelp.com/v3/businesses/search

class SearchTerm(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    term = models.CharField(max_length=500)

    def __str__(self):
        return self.user + " - " + self.term

class NumberOfSearches(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    total = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.user + " - " + self.total

class Favourites(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    favourite = models.CharField(max_length=500)

    def __str__(self):
        return self.user + " - " + self.favourite
