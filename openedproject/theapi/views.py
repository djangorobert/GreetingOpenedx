from rest_framework import viewsets
from theapi.models import Greeting
from theapi.serializers import GreetingSerializer
from django.shortcuts import render

# View for Homepage.


def home(request):
    # A query that gets all greeting post from newest to oldest.
    recent_greetings = Greeting.objects.all()
    # Query that only gets the newest greeting post and only that one.
    last_added_greeting = Greeting.objects.first()
    context = {
        'recent_greetings': recent_greetings,
        'last_added_greeting': last_added_greeting,
    }
    return render(request, 'theapi/home.html', context)

# View for API.


class GreetingViewSet(viewsets.ModelViewSet):
    queryset = Greeting.objects.all()
    serializer_class = GreetingSerializer
