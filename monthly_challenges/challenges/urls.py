from django.urls import path
from . import views

urlpatterns = [
    path('', views.index), #/challenge/ months menu
    path('<int:month>', views.monthly_challenge_by_number), # used when there is a number in the url ex /challenge/1
    path('<str:month>', views.montlhy_challenge, name='month-challenge') # returns the value of the respective month
]