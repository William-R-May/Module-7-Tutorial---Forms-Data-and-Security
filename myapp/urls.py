from django.urls import path
from . import views

app_name = 'myapp'

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('profile/', views.profile, name='profile'),
    path('book/<int:pk>/', views.book_detail, name='book_detail'),
]
