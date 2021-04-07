from django.urls import path 
#2. adding import for views 4/7/2021 
from . import views 

urlpatterns = [
    #3. adding path to get index.html 4-7-2021 
    path('', views.index, name='index'), 

]