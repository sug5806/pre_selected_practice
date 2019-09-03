from django.urls import path

from .views import *

urlpatterns = [
    path('sel/', sel, name='sel'),
    path('pre/', pre, name='pre'),
]
