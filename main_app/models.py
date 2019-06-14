from django.db import models
from django.urls import reverse


class Player:
    def __init__(self, name, age):
        self.name = name
        self.age = age

players = [
    Player('Lolo', 3),
    Player('Raven', 4),
]