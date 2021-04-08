from django.shortcuts import render

# Create your views here.
#1. created the first view, a index.html file 4-7-2021 ~urls.py in Club app 
def index(request): 
    return render(request, 'Club/index.html') 