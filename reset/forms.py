from django.contrib.auth.forms import PasswordResetForm,SetPasswordForm
from django import forms
 

class passwordresetform(PasswordResetForm):
     email = forms.EmailField(label="Email", max_length=254, widget=forms.EmailInput(attrs={"autocomplete": "email",'class':'form-control resetemail'}),
    )



class setpasswordform(SetPasswordForm):
    new_password1 = forms.CharField(label="New password",widget=forms.PasswordInput(attrs={"autocomplete": "new-password",'class':'form-control newpass1'}))

    new_password2 = forms.CharField(
        label="New password confirmation",
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password",'class':'form-control newpass1'}))