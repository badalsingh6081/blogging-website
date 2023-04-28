from django.shortcuts import render,redirect

from . forms import passwordchangeform,setpasswordform,setpasswordforms
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
 



## change password ( using old password)
def user_change_pass(request):
    if request.user.is_authenticated:
     if request.method=='POST':
        fm=passwordchangeform(user=request.user,data=request.POST)
        if fm.is_valid():
            fm.save()
            update_session_auth_hash(request,fm.user) ## (use for - password change hone ke baad profile.html me send kr de)
            messages.success(request,'Password change Successfully')
            return redirect('/acc/profile/')
        else:
            update_session_auth_hash(request,fm.user) ## (use for - password change hone ke baad profile.html me send kr de)
            messages.warning(request,'Please re-enter your Password')
            return redirect('/acc/profile/')

     else:    
        fm=passwordchangeform(user=request.user)
     return render(request,'change/changepass.html',{'form':fm})
    else:
       return redirect('/login/')




##----------------------------------------------------------------------------------------------------      #  

##  reset password

from django.shortcuts import render
from django.shortcuts import redirect
import smtplib,random
from django.contrib.auth.models import User
from django.core.cache import cache  




def user_reset_pass(request):
    if request.user.is_authenticated:
        if request.method=='POST':
           fm=setpasswordform(user=request.user,data=request.POST)
           if fm.is_valid():
               fm.save()
               update_session_auth_hash(request,fm.user) ## (use for - password change hone ke baad profile.html me send kr de)
               messages.success(request,'Password Reset Successfully')
               return redirect('/acc/profile/')
   
        else: 
            verify2=cache.get('verify2')
            if verify2 != None:   
                fm=setpasswordform(user=request.user)
     
                return render(request,'change/resetpass.html',{'form':fm})
            else:
                return redirect('/acc/resetemail')    
    else:
        return redirect('/acc/login/')

# def user_reset_pass(request):
#         if request.method=='POST': 
#            username=request.POST['username']
#            user=User.objects.get(username=username)
#            fm=setpasswordforms(user=username,data=request.POST)
#            if fm.is_valid():
#                fm.save()
#             #    update_session_auth_hash(request,fm.user) ## (use for - password change hone ke baad profile.html me send kr de)
#                return redirect('acc/login/')
   
#         else:   
           
#            fm=setpasswordforms(user=)
#         return render(request,'change/resetpass.html',{'form':fm})
    



def user_reset_email(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            email=request.POST.get('email')
            uname=request.POST.get('username')
            user=User.objects.filter(username=uname).first()
            if user != None:
                useremail=user.email
                if useremail == email:
                    cache.set('email',email,100)
                    # request.session['uname']=uname
                    # cache.set('uname',uname,100)
                    get(request,email)  
                    cache.set('verify','verify',100)
                    messages.success(request,'Otp Sent Successfully')
                    return redirect('/acc/otp2/')
                else:
                    messages.warning(request,'Email doesn,t matched with this username')    
                    return redirect('/acc/resetemail/')
            else:
                messages.warning(request,'Username not found')    
                return redirect('/acc/resetemail/')

        else: 
            return render(request,'change/resetemail.html')
    return redirect('/acc/login/')








def ot2(request):
    if request.user.is_authenticated:
        if request.method == 'POST':     
            otp2= request.POST.get('otp')
            if otp2 != None:
                mv=cache.get('otp2')        
                if otp2 == mv:
                    cache.clear
                    cache.set('verify2','verify2',60)
                    return redirect('/acc/resetpass/')
                else:
                    messages.warning(request,'Please enter correct   otp')
                    return redirect('/acc/otp2/')    
    
            else:
                messages.warning(request,'Please enter   otp')
                return redirect('/acc/otp2/')    
        else:
            verify=cache.get('verify')
            if verify != None:
                return render(request,'change/otp2.html')        
            else:
                return redirect('/acc/resetemail/')
            
    else:
        return redirect('/acc/login/')


           












def resend2(request):
    email=cache.get('email')
    if email != None:
        time=cache.get('time')
        if time != '60':
            if email != None:
               get(request,email)
               messages.success(request,'Resend otp successfully' )
               return redirect('/acc/otp2/')
            else:
               messages.warning(request,'Your session expire' )
               return redirect('/acc/resetemail/')

        else: 
            messages.warning(request,'Resend otp after 60 second of your  submission')
            return redirect('/acc/otp2/')  
    else:
        return redirect('/acc/resetemail/')







def get(request,email):
        server=smtplib.SMTP('smtp.gmail.com',587)
        server.starttls()
        server.login('badalsinghaira273@gmail.com','dvdukzhxiuhlfara')
        otp2 = str(random.randint(1000,9999))
        # request.session['otp']=otp

        cache.set('otp2',otp2,60)
        cache.set('time','60',60)
        # request.session.set_expiry(100)
        msg = 'Hello , Your OTP is ' + str(otp2)
        server.sendmail('badalsinghaira273@gmail.com',email,msg)
        server.quit()


       


def otp2(request):
    verify=cache.get('verify')
    if verify != None:
        return render(request,'change/otp.html')        
    else:
        return redirect('/acc/resetemail/')




