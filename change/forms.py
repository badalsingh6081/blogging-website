
from django.contrib.auth.forms import PasswordChangeForm,SetPasswordForm,UserCreationForm
from django import forms
from django.utils.translation import gettext,gettext_lazy as _





class setpasswordform(SetPasswordForm):
    new_password1 = forms.CharField(
        label="New password",
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password",'class':'form-control newpass1'}),
       
    )

    new_password2 = forms.CharField(
        label="New password confirmation",
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password",'class':'form-control newpass1'}),
        
    )
    


class setpasswordforms(SetPasswordForm):
    username = forms.CharField(
        label="username",
        widget=forms.TextInput(attrs={'class':'form-control newpass1'}),
       
    )
    new_password1 = forms.CharField(
        label="New password",
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password",'class':'form-control newpass1'}),
       
    )

    new_password2 = forms.CharField(
        label="New password confirmation",
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password",'class':'form-control newpass1'}),
        
    )















class passwordchangeform(PasswordChangeForm):
    old_password = forms.CharField(
        label='Old password',
    
        widget=forms.PasswordInput(
            attrs={"autocomplete": "current-password",'class':'form-control oldpass', "autofocus": True}
        ),
    )



    new_password1 = forms.CharField(
        label="New password",
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password ",'class':'form-control newpass1'}),
       
    )
    new_password2 = forms.CharField(
        label="New password confirmation",
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password ",'class':'form-control newpass1'}),
        
    )
    