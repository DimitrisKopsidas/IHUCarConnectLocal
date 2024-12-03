from django.urls import path
from . import views

urlpatterns = [
 path('light/', views.light_view, name='light'),
]
