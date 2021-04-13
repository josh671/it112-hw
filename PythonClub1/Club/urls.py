from django.urls import path 
#2. adding import for views 4/7/2021 
from . import views 

urlpatterns = [
    #3. adding path to get index.html 4-7-2021 
    path('', views.index, name='index'), 
    #4 adding url path for views.py resources 4-13-2021
    path('resource/', views.resource, name='resource'), 
    #5 go create resource.html
]