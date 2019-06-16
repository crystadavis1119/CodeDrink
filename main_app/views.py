from django.shortcuts import render
from django.http import HttpResponse

class Player:
    def __init__(self, name, breed, description, age):
        self.name = name
        self.breed = breed
        self.description = description
        self.age = age

players = [
    Player('Lolo', 'tabby', 'foul little demon', 3),
    Player('Sachi', 'tortoise shell', 'diluted tortoise shell', 0),
    Player('Raven', 'black tripod', '3 legged cat', 4)
]


def home(request):
  return HttpResponse('<h1>Code Drink Homepage</h1>')

def game(request):
  return render(request, 'game.html')

def players_index(request):
    return render(request, 'players/index.html', { 'players' : players })