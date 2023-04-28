from django.shortcuts import render

# Create your views here.
def nav(request):
    return render(request,'core/navbar.html')

    s