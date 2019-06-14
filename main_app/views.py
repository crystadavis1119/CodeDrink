from django.shortcuts import render
from django.http import HttpResponse
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
      return redirect('index')
    else:
      error_message = 'Invalid credentials - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

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