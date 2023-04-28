
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm
from django import forms








## for user== profile page
class EditUserProfileForm(UserChangeForm):
    password =None
    class Meta:
        model=User
        fields=['username','first_name','last_name','email','date_joined','last_login']
        labels={'email':'Email'}
        widgets={
            'username':forms.TextInput(attrs={'class':'form-control'}),

            'first_name':forms.TextInput(attrs={'class':'form-control'}),

            'last_name':forms.TextInput(attrs={'class':'form-control'}),

            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'date_joined':forms.DateTimeInput(attrs={'class':'form-control'}),

            'last_login':forms.DateTimeInput(attrs={'class':'form-control'}),
            
         }

     








## for admin== profile page
class EditAdminProfileForm(UserChangeForm):
    password =None
    class Meta:
        model=User
        fields=['username','first_name','last_name','email','date_joined','last_login','is_staff','is_active']
        labels={'email':'Email'}
        widgets={
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'first_name':forms.TextInput(attrs={'class':'form-control'}),
            'last_name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'date_joined':forms.DateTimeInput(attrs={'class':'form-control'}),
            'last_login':forms.DateTimeInput(attrs={'class':'form-control'}),
            'is_staff':forms.CheckboxInput(attrs={'class':'staff'}),
            'is_active':forms.CheckboxInput(attrs={'class':'active'}),
         }
