from django.shortcuts import render,HttpResponseRedirect
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from Post.models import blog
from . forms import EditAdminProfileForm,EditUserProfileForm

def user_login(request):
    context={'login':'active'} 
    if not request.user.is_authenticated:
        if request.method == 'POST':
            username=request.POST.get('username')
            password=request.POST.get('password')
            first=User.objects.filter(username=username).first()
            if first != None:
                user=authenticate(username=username,password=password)
                if user is not None:
                    login(request,user)
                    messages.success(request,'login succesfully')
                    return redirect('/acc/dashboard/')
                else:
                    messages.warning(request,'Please enter correct   password')
                    return redirect('/acc/login/')

            else:
                messages.warning(request,'Please enter correct username')
                return redirect('/acc/login/')

        else:
            return render(request,'log/login.html',context)


    else:
        return redirect('/acc/dashboard/')




## logout
def user_logout(request):
    
    logout(request) 
    messages.success(request,'Logout successfully')   
    return redirect('/acc/login/')



































## profile page for user
def user_profile(request):
    if request.user.is_authenticated:
       if request.method == 'POST':
         
          fm=EditUserProfileForm(request.POST,instance=request.user)
        
          if fm.is_valid():
             fm.save()
             messages.success(request,'profile update successfully')
       else:      
          fm=EditUserProfileForm(instance=request.user)
        
       return render(request,'log/profile.html',{'name':request.user,'form':fm})
    else:
        return redirect('/acc/login/')


## profile for admin
def admin_profile(request):
    if request.user.is_authenticated:
       if request.method == 'POST':
        
            fm=EditAdminProfileForm(request.POST,instance=request.user)
            users=User.objects.all()
      
            if fm.is_valid():
               fm.save()
               messages.success(request,'Profile update successfully')
               return redirect('/acc/adminprofile/')
            else:
               messages.warning(request,'Please enter valid data')
               return redirect('/acc/adminprofile/')


       else:   
          
            fm=EditAdminProfileForm(instance=request.user)
            users=User.objects.all()
          
       return render(request,'log/adminprofile.html',{'name':request.user,'form':fm, 'users':users})
    else:
        return redirect('/acc/login/')

















## Dashboard of user
def user_detail(request,pk):
   if request.user.is_authenticated:
        if request.user.is_superuser == True:
            pi = User.objects.get(pk=pk)
            fm=EditAdminProfileForm(instance=pi)
            return render(request,'log/userdetail.html',        {'form':fm,     'user':pi})
        else:
            return redirect('/acc/profile/') 

   else:
      return redirect('/acc/login/') 




## delte by admin
def user_delete(request,pk):
    if request.user.is_authenticated:
        if request.user.is_superuser == True:
            user = User.objects.get(pk=pk)
            user.delete()
            messages.success(request,'User deleted successfully')
            return redirect('/acc/adminprofile/')
        else:
            return redirect('/acc/profile/') 

    else:
       return redirect('/login/') 
         






        
def user_dashboard(request):
    if request.user.is_authenticated:
        posts=blog.objects.filter(user_id=request.user.id)
          
        return render(request,'log/dashboard.html',{'posts':posts,'dashboard':'active'})
    else:
        return redirect('/acc/login/')





             