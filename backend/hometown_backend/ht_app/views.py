from django.shortcuts import render
from rest_framework import generics
from ht_app.models import Community
from ht_app.serializers import CommSerializer

# Create your views here.
class CommListAPIView(generics.ListAPIView):
    queryset = Community.objects.all()
    serializer_class = CommSerializer

class CommDetailAPIView(generics.RetrieveAPIView):
    queryset = Community.objects.all()
    serializer_class = CommSerializer