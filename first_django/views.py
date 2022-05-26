from .models import Person
from .serializers import PersonSerializer
from rest_framework import generics, mixins, permissions 

class PersonListCreateAPIView(generics.ListCreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer