from django.urls import path
from . import views
urlpatterns = [
    path('nav/', views.nav,name='nav'),
]
