from django.urls import path
from . import views

urlpatterns = [
    # When the user hits the root path, run the 'index' function from views.py
    path('', views.index, name='index'),
]