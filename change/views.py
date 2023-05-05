import random
import smtplib
from django.core.cache import cache
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.shortcuts import render
from django.shortcuts import render, redirect

from . forms import passwordchangeform
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash


# change password ( using old password)
def user_change_pass(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            fm = passwordchangeform(user=request.user, data=request.POST)
            if fm.is_valid():
                fm.save()
                # (use for - password change hone ke baad profile.html me send kr de)
                update_session_auth_hash(request, fm.user)
                messages.success(request, 'Password change Successfully')
                return redirect('/acc/profile/')
            else:
                # (use for - password change hone ke baad profile.html me send kr de)
                update_session_auth_hash(request, fm.user)
                messages.warning(request, 'Please re-enter your Password')
                return redirect('/acc/profile/')

        else:
            fm = passwordchangeform(user=request.user)
        return render(request, 'change/changepass.html', {'form': fm})
    else:
        return redirect('/login/')

