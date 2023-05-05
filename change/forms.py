
from django.contrib.auth.forms import PasswordChangeForm
from django import forms




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
    