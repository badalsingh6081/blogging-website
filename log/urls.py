from django.urls import path
from . import views
urlpatterns = [
    path('login/', views.user_login,name='login'),
    path('logout/', views.user_logout,name='logout'),
    path('dashboard/', views.user_dashboard,name='dashboard'),
    path('profile/', views.user_profile,name='profile'),
    path('adminprofile/', views.admin_profile,name='adminprofile'),
    path('userdetail/<int:pk>', views.user_detail,name='userdetail'),
    path('userdelete/<int:pk>', views.user_delete,name='userdelete'),
 
]
