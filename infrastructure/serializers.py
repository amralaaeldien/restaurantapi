from . import models
from rest_framework import serializers

class RateSerializer(serializers.HyperlinkedModelSerializer):
	url = serializers.HyperlinkedIdentityField(view_name='rate-detail', read_only=True)
	class Meta:
		model = models.Rate
		fields = ['id', 'url','restaurant', 'rating']


class TableSerializer(serializers.HyperlinkedModelSerializer):
	url = serializers.HyperlinkedIdentityField(view_name='table-detail', read_only=True)
	class Meta:
		model = models.Table
		fields = ['id', 'url', 'restaurant', 'num_seats', 'reserved']

class RestaurantSerializer(serializers.HyperlinkedModelSerializer):
	url = serializers.HyperlinkedIdentityField(view_name='restaurant-detail', read_only=True)

	class Meta:
		model = models.Restaurant
		fields = ['id', 'url', 'name', 'image', 'category', 'price', 'overall_rating', 'table_set', 'rate_set']



