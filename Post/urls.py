from django.urls import path
from . import views
urlpatterns = [
    path('addpost/', views.add_post,name='addpost'),
    path('', views.blogs,name='blogs'),
    path('editpost/<int:pk>', views.edit_post,name='editpost'),
]
