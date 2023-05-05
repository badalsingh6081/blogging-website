from django.shortcuts import render
from django.shortcuts import redirect
import smtplib,random
from django.contrib.auth.models import User
from django.core.cache import cache  
from django.contrib import messages
# from django.utils.translation import gettext,gettext_lazy as _  

    

def sign_up(request):
    context={'signup':'active'}
    if request.method == 'POST':
        name= request.POST.get('fullname')
        username= request.POST.get('username')
        email= request.POST.get('email')
        lastname= request.POST.get('lastname')
        password= request.POST.get('password')
        passwords= request.POST.get('passwords')
        first=User.objects.filter(username=username).first()
        second=User.objects.filter(email=email).first()
        
        if first is  None :
            if second is None:

                if password==passwords:
                    
                    user=User(first_name=name,username=username,     email=email,    last_name=lastname)
                    user.set_password(password)
                    cache.set('user',user,70)
                    # request.session['user']=user
                    cache.set('email',email,70)
                    # request.session['email']=email
                    
                    get(request,email)
                    cache.set('verify','verify',70)
                    messages.success(request,'Otp Sent  , if not please enter correct email or resend otp')
                    return redirect('/acc/otp/')
                
                else:
                    messages.warning(request,"Password din't match , Please enter correct confirmation password ")
                    return redirect('/acc/signup/')    
            else:
                messages.warning(request,"User already registered with this email , Please enter another email")
                return redirect('/acc/signup/')    

            
        else:
            messages.warning(request,'Uaername Alredy Registered,  Please Enter Different Username')
            return redirect('/acc/signup/')      
    return render(request,'sign/signup.html',context)






def ot(request):
    if request.method == 'POST':     
        otp= request.POST.get('otp')
        if otp != None:
            mv=cache.get('otp')            
            if otp == mv:
                user=cache.get('user')
                # user=request.sesssion['user']
                user.save()
                cache.clear
                # request.session.flush()
                messages.success(request,'Account Created Successfully')
                return redirect('/acc/login/')
            else:
                messages.warning(request,'Please enter correct otp')
                return redirect('/acc/otp/')
        else:
            messages.warning(request,'Please enter   otp')
            return redirect('/acc/otp/')  
    else:        
        return redirect('/acc/otp/')





    
def resend(request):
    email=cache.get('email')
    # time = request.session['time']
    if email != None:

        time=cache.get('time')
    
        if time != '60':
            if email != None:
                get(request,email)
                messages.success(request,'Resend otp     successfully' )
                return redirect('/acc/otp/')
            else:
               messages.warning(request,'Your session expire' )
               return redirect('/acc/signup/')

        else:
            messages.warning(request,'Resend otp after 60 second')
            return redirect('/acc/otp/')    
    else:
        return redirect('/acc/signup/')    




def get(request,email):
        server=smtplib.SMTP('smtp.gmail.com',587)
        server.starttls()
        server.login('badalsinghaira273@gmail.com','dvdukzhxiuhlfara')
        otp = str(random.randint(1000,9999))

        cache.set('otp',otp,60)
        cache.set('time','60',60)
        # request.session['time']='60'
        # request.session.set_expiry(60)
        msg = 'Hello , Your OTP is ' + str(otp)
        server.sendmail('badalsinghaira273@gmail.com',email,msg)
        server.quit()










def otp(request):
    verify=cache.get('verify')
    if verify != None:
        return render(request,'sign/otp.html')        
    else:
        return redirect('/acc/signup/')





