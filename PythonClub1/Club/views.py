
from django.shortcuts import render, get_object_or_404
#1.  inpoorting Product from .models 4-13-2021 
from .models import Meeting, MeetingMinutes, Resources, Event
from django.urls import reverse_lazy
#adding form stuff 5-31-2021
from .forms import MeetingForm, ResourceForm, Resources
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

def meetings(request): 
    meeting_list=Meeting.objects.all() 
    return render(request, 'Club/meetings.html', {'meeting_list': meeting_list})


#**Asignment 6 start 4-19-2021
#add views for assignment 6 
def meetingDetail(request, id): 
    #1. assign meeting get object 4-19-2021
    meetingDetail=get_object_or_404(Meeting, pk=id) #assing meeting the primary key id's from Meeting table 
    #2. return the render statment for meetingdetail.html
    return render(request, 'Club/meetingDetail.html', {'meetingDetail': meetingDetail})
    #3. ADD inport for get_object_or_404(Meeting, pk=id) after render
    #4. go and set paths in url 4-19-2021 

def newMeeting(request): 
    form=MeetingForm 
    if request.method =='POST': 
        form=MeetingForm(request.POST)
        if form.is_valid(): 
            post=form.save(commit=True)
            post.save() 
            form=MeetingForm() 
    else: 
        form=MeetingForm 
    return render(request, 'Club/newmeeting.html', {'form': form}) 


def newResource(request): 
    form=ResourceForm 
    if request.method =='POST': 
        form=ResourceForm (request.POST)
        if form.is_valid(): 
            post=form.save(commit=True)
            post.save() 
            form=ResourceForm () 
    else: 
        form=ResourceForm  
    return render(request, 'Club/newmeeting.html', {'form': form}) 