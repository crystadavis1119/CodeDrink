from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

COLOR = [
    ('BLUE', 'Blue'),
    ('RED', 'Red'),
    ('YELLOW', 'Yellow'),
    ('GREEN', 'Green'),
    ('ORANGE', 'Orange'),
    ('PURPLE', 'Purple'),
]

class Player(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    color = models.CharField(
        max_length=10, 
        choices=COLOR, 
        default=COLOR[0][0]
    )
    description = models.TextField(max_length=250)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    # Return back to detail page after profile
    def get_absolute_url(self):
        return reverse('detail', kwargs={'player_id': self.id})