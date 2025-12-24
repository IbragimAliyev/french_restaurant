from django.shortcuts import render
from rest_framework import generics
from .models import Section, Dish, Reservation
from .serializers import SectionSerializer, DishSerializer, ReservationSerializer
# Create your views here.

class SectionListView(generics.ListAPIView):
    queryset = Section.objects.all()
    serializer_class = SectionSerializer

class DishListView(generics.ListAPIView):
    queryset = Dish.objects.all()
    serializer_class = DishSerializer


class ReservationListView(generics.ListCreateAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
