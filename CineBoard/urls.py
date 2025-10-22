from django.urls import path
from . import views

app_name = 'cineboard'

urlpatterns = [
    path('', views.FilmListView.as_view(), name='film_list'),
    path('film/<int:pk>/', views.film_detail, name='film_detail'),
    path('film/add/', views.film_create, name='film_create'),
    path('film/<int:pk>/edit/', views.film_edit, name='film_edit'),
    path('film/<int:pk>/delete/', views.film_delete, name='film_delete'),

    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]
