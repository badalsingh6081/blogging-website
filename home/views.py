from django.shortcuts import render
from Post.models import blog
# Create your views here.
def home(request):
    context={'home':'active'}
    post = blog.objects.all()
    return render(request,'home/home.html',{'posts':post},context)