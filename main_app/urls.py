from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('game/', views.game, name='game'),
    path('result/', views.result, name ='result'),
    path('create/', views.create, name='create'),
    path('profile/< int : pk >/', views.profile, name='profile'),
    # path('profile/< int:pk >/update/', views.ProfileUpdate.as_view(), name='profile_update'),
    # path('profile/< int:pk >/delete/', views.ProfileDelete.as_view(), name='profile_delete'),

]
