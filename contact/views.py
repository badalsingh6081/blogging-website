
from django.shortcuts import render,redirect
from .models import Contact
from django.contrib import messages

# Create your views here.
def contact(request):
    context={'contact':'active'}
    if request.method == 'POST':
        name=request.POST.get('name')
        phone=request.POST.get('phone')
        email=request.POST.get('email')
        message=request.POST.get('message')
        
        contact=Contact(name=name,phone=phone,email=email,message=message)
        if contact != None:
            contact.save()
            messages.success(request,'Contact saved')
            return redirect('/acc/contact/')
        else:
            messages.warning(request,'All fields are mandatory')
            return redirect('/acc/contact/')

    else:
        return render(request,'contact/contact.html',context)
        

    




