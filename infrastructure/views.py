from django.shortcuts import render

# Create your views here.
from .models import Restaurant, Rate, Table
from .serializers import RestaurantSerializer, RateSerializer, TableSerializer
from rest_framework import generics


class RestaurantList(generics.ListCreateAPIView):
	queryset = Restaurant.objects.all()
	serializer_class = RestaurantSerializer


class RestaurantDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Restaurant.objects.all()
	serializer_class = RestaurantSerializer

class RateList(generics.ListCreateAPIView):
	serializer_class = RateSerializer

	def get_queryset(self):
		queryset = Rate.objects.all().filter(restaurant__pk = self.kwargs['pk'])
		return queryset


class RateDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Rate.objects.all()
	serializer_class = RateSerializer

class TableList(generics.ListCreateAPIView):
	serializer_class = TableSerializer

	def get_queryset(self):
		queryset = Table.objects.all().filter(restaurant__pk = self.kwargs['pk'])
		return queryset


class TableDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Table.objects.all()
	serializer_class = TableSerializer