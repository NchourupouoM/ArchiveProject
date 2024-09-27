from django.shortcuts import render

# Create your views here.


def home(request):
    message = "Bienvenu"
    return render(request,'archives/home.html', {"message": message})