from .forms import passwordresetform,setpasswordform
from django.contrib.auth.views import PasswordResetView,PasswordResetConfirmView,PasswordResetDoneView,PasswordResetCompleteView
from django.shortcuts import render, redirect
from django.contrib.auth.forms import SetPasswordForm,PasswordResetForm
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
# Create your views here.










class passwordresetview(PasswordResetView):
        template_name='myapp/password_reset_form.html'
        form_class=passwordresetform

class passwordresetdone(PasswordResetDoneView):
        template_name='myapp/password_reset_done.html'
        

class passwordresetconfirm(PasswordResetConfirmView):
        template_name='myapp/password_reset_confirm.html'
        form_class=setpasswordform

class passwordresetcomplete(PasswordResetCompleteView):
        template_name='myapp/password_reset_complete.html'






























