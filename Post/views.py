from django.shortcuts import render,redirect
from .models import blog
from django.contrib import messages

# Create your views here.
def add_post(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            name=request.POST.get('name')
            date=request.POST.get('date')
            title=request.POST.get('title')
            desc=request.POST.get('desc')
            
            post=blog(user=request.user,name=name,date=date,title=title,desc=desc)
            post.save()
            messages.success(request,'Post added succesfully')
            return redirect('/acc/dashboard/')
        else:
            return render(request,'post/addpost.html')
    else:
        return redirect('/acc/login/')        





def blogs(request):
    
    post=blog.objects.all()
    if post != None:
       return render(request,'post/blogs.html',{'posts':post,'home':'active'})  
    else:
       context={'msg':'Post not found','home':'active'}     
       return render(request,'post/blogs.html',context)    







    
def edit_post(request,pk):
    if request.user.is_authenticated:
      if request.method == 'POST':
        name=request.POST.get('name')
        date=request.POST.get('date')
        title=request.POST.get('title')
        desc=request.POST.get('desc')
        post=blog.objects.filter(id=pk).update(name=name,date=date,title=title,desc=desc)
        
        return redirect('/acc/dashboard/')
      else:
        post=blog.objects.get(id=pk)
      

    else:
        return redirect('/acc/login/')
    return render(request,'post/editpost.html',{'post':post})