from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Player
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('players_create')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)


class PlayerCreate(LoginRequiredMixin, CreateView):
  model = Player
  fields = ['name', 'age', 'color', 'description']
  success_url = '/players/'

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)


class PlayerUpdate(LoginRequiredMixin, UpdateView):
  model = Player
  fields = ['age', 'color', 'description']

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)


class PlayerDelete(LoginRequiredMixin, DeleteView):
  model = Player
  success_url = '/players/'

def home(request):
  return render(request, 'home.html')

def game(request):
  players = Player.objects.all()
  return render(request, 'game.html', { 'players' : players })

def players_index(request):
  players = Player.objects.all()
  return render(request, 'players/index.html', { 'players' : players })

def players_detail(request, player_id):
  player = Player.objects.get(id=player_id)
  return render(request, 'players/detail.html', { 'player': player })

def results(request):
  players = Player.objects.all()
  return render(request, 'results.html', { 'players' : players })
