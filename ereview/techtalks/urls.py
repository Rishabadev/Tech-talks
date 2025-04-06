from django.urls import path 
from . import views
app_name = 'techtalks'

urlpatterns = [
    path('home/', views.home, name='home'),
    
]