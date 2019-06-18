from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Player(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    age = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    # Return back to detail page after profile
    def get_absolute_url(self):
        return reverse('detail', kwargs={'player_id': self.id})