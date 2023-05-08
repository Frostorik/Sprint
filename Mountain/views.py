from rest_framework import generics
from .serializers import PerevalAddedSerializer
from .models import PerevalAdded


class SubmitData(generics.CreateAPIView):
    queryset = PerevalAdded.objects.all()
    serializer_class = PerevalAddedSerializer
