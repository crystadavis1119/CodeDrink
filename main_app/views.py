from django.shortcuts import render
from django.http import HttpResponse

# Define the home view
def home(request):
  return HttpResponse('<h1>Code Drink Homepage</h1>')

def game(request):
  return HttpResponse('<h1>Code Drink Game</h1>')

def result(request):
  return HttpResponse('<h1>You Drink NOW!</h1>')

def create(request):
  return HttpResponse('<h1>Create Profile</h1>')

def profile(request, player_id):
    player = Player.objects.get(id = player_id)
    return render(request, 'players/profile.html')