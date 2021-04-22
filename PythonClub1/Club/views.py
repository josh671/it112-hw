from django.shortcuts import render, get_object_or_404
#1.  inpoorting Product from .models 4-13-2021 
from .models import Meeting, MeetingMinutes, Resources, Event
from django.urls import reverse_lazy

# Create your views here.
#1. created the first view, a index.html file 4-7-2021 ~urls.py in Club app 
def index(request): 
    return render(request, 'Club/index.html') 

#adding product views 4-13-2021 
#2. creating products function that takes request 4-13-2021
def resource(request): 
    #3. create a list called resource_list 4-13-2021
    resource_list = Resources.objects.all() #gett all objects from resources table
    return render(request, 'Club/resource.html', {'resource_list': resource_list}) #render result on resources.html 
#4. add URL to urls.py 4-13-2021 

def meeting(request): 
    meetings=Meeting.objects.all() 
    return (render(request, 'Club/meeting.html', {'meeting': meeting}))


#**Asignment 6 start 4-19-2021
#add views for assignment 6 
def meetingDetail(request, id): 
    #1. assign meeting get object 4-19-2021
    meeting=get_object_or_404(Meeting, pk=id) #assing meeting the primary key id's from Meeting table 
    #2. return the render statment for meetingdetail.html
    return render(request, 'Club/meetingDetail.html', {'meeting': meeting})
    #3. go and set paths 4-19-2021