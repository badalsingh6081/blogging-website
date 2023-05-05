from django.urls import path
from . import views
urlpatterns = [
    path('changepass/', views.user_change_pass,name='changepass')
]
