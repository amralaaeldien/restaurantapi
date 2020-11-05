from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('restaurants/', views.RestaurantList.as_view()),
    path('restaurants/<int:pk>/', views.RestaurantDetail.as_view(), name='restaurant-detail'),
    path('restaurants/<int:pk>/rates/', views.RateList.as_view()),
    path('restaurants/rates/<int:pk>/', views.RateDetail.as_view(), name='rate-detail'),
    path('restaurants/<int:pk>/tables/', views.TableList.as_view()),
    path('restaurants/tables/<int:pk>/', views.TableDetail.as_view(), name='table-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)