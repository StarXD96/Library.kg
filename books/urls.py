from django.urls import path
from . import views


urlpatterns = [
    path('', views.book_list_view, name='book_list'),
    path('book_detail/<int:id>/', views.book_detail_view, name='book_detail'),
    path('current_time/', views.current_time_view, name='current_time'),
    path('random_number/', views.random_number_view, name='random_number'),
    path('about_myself/', views.about_myself_view, name='about_myself'),
]