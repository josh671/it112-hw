from django.urls import path 
#2. adding import for views 4/7/2021 
from . import views 

urlpatterns = [
    #3. adding path to get index.html 4-7-2021 
    path('', views.index, name='index'), 
    #4 adding url path for views.py resources 4-13-2021
    path('resource/', views.resource, name='resource'), 
    #5 go create resource.html

    path('meeting/', views.meeting, name='meeting'),

    #3. go and set paths 4-19-2021 
    #passing integer that is id, we are getting id from views 
    path('meetingDetail/<int:id>', views.meetingDetail, name='detail'),
    #go club and make product detail.html 4-19-2021
]