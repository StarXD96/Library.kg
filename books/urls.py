from django.urls import path
from . import views


urlpatterns = [
    path('current_time/', views.current_time_view, name='current_time'),
    path('random_number/', views.random_number_view, name='random_number'),
    path('about_myself/', views.about_myself_view, name='about_myself'),
]