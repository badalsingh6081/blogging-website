from django.urls import path
from . import views
urlpatterns = [
    path('changepass/', views.user_change_pass,name='changepass'),
    path('resetpass/', views.user_reset_pass,name='resetpass'),
    path('resetemail/', views.user_reset_email,name='resetemail'),
    path('otp2/', views.otp2,name='otp2'),
    path('ot2/', views.ot2,name='ot2'),
    path('resend2/', views.resend2,name='resend2'),
]
