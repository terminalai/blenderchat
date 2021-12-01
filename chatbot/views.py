# from django.shortcuts import render
from rest_framework import generics
from .models import Message
from .serializers import MessageSerializer

# Create your views here.


class ListMessage(generics.ListAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


class DetailMessage(generics.RetrieveAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
