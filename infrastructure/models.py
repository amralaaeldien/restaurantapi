from django.db import models
from django.db.models import Avg
from django.urls import reverse


# Create your models here.
class Restaurant(models.Model):
	name = models.CharField(max_length=100)
	image = models.ImageField(upload_to='media/')
	category = models.CharField(max_length=100)
	price = models.IntegerField()
	overall_rating = models.IntegerField()

	def get_overall_rating(self):
		average_rating = self.rate_set.aggregate(rating =Avg('rating'))['rating']
		return int(average_rating)

	def get_absolute_url(self):
		return reverse('restaurant-detail',args=[str(self.id)])

	def __str__(self):
		return self.name

class Rate(models.Model):
	restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
	rating = models.IntegerField()
	
	def save(self, *args, **kwargs):
		super(Rate, self).save(*args, **kwargs)
		self.restaurant.overall_rating = self.restaurant.get_overall_rating()
		self.restaurant.save()

	def __str__(self):
		return self.restaurant.name

	def get_absolute_url(self):
		return reverse('rates-detail',args=[str(self.id)])

class Table(models.Model):
	restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
	num_seats = models.IntegerField()
	reserved = models.BooleanField(default=False)
	
	def __str__(self):
		return self.restaurant.name

	def get_absolute_url(self):
		return reverse('tables-detail',args=[str(self.id)])