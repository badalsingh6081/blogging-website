from django.urls import path
from . import views
urlpatterns = [
    path('signup/', views.sign_up,name='signup'),
    path('otp/', views.otp,name='otp'),
    path('ot/', views.ot,name='ot'),
    path('resend/', views.resend,name='resend'),
]
