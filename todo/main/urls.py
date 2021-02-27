from django.urls import path

from main.views import *

urlpatterns = [
    path('todos/', todo),
    path('todos/1/completed/', completed)
]