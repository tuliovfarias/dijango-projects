from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:month>", views.numb_challenges),
    path("<str:month>", views.monthly_challenge, name="month-challenge")
]

