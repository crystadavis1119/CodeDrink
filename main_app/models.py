from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

AGE= [
    (21, '21'),
    (22, '22'),
    (23, '23'),
    (24, '24'),
    (25, '25'),
    (26, '26'),
    (27, '27'),
    (28, '28'),
    (29, '29'),
    (30, '30'),
    (31, '31'),
    (32, '32'),
    (33, '33'),
    (34, '34'),
    (35, '35'),
    (36, '36'),
    (37, '37'),
    (38, '38'),
    (39, '39'),
    (40, '40+'),
]

COLOR = [
    ('BLUE', 'Blue'),
    ('RED', 'Red'),
    ('YELLOW', 'Yellow'),
    ('GREEN', 'Green'),
    ('ORANGE', 'Orange'),
    ('PURPLE', 'Purple'),
]

DRINK = [
    ('BEER', 'I crush brews'),
    ('WINE', "I love sippin' on some vino"),
    ('LIQUOR', 'Give me the hard stuff'),
    ('NONE', "Drinking isn't really my thing"),
]

class Player(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(
        choices=AGE, 
        default=AGE[0][0]
    )
    color = models.CharField(
        max_length=10, 
        choices=COLOR, 
        default=COLOR[0][0]
    )
    drink = models.CharField(
        max_length=30, 
        choices=DRINK, 
        default=DRINK[0][0]
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    # Return back to detail page after profile
    def get_absolute_url(self):
        return reverse('detail', kwargs={'player_id': self.id})