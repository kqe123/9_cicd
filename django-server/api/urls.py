from django.urls import path
from .views import HelloWorldView

# localhost:8000/api/*
urlpatterns = [
    # localhost:8000/api/helloworld/
    path('helloworld/', HelloWorldView.as_view(), name='api-helloworld'),
]
