from django.db import models
#user models must be imported 
#1. importing user as a model 4-8-2021
from django.contrib.auth.models import User


#models are what become tables in a database
# Create your models here.
#2. first class 4-8-2021 
class Meeting(models.Model): 
    MeetingTitle = models.CharField(max_length=255) 
    MeetingDate = models.DateField() 
    MeetingTime = models.TimeField() 
    MeetingLocation = models.TextField()
    Agenda = models.TextField(null=True, blank=True) #means that we can leave blank 
    

    #3. two string method and created the class Meta 4-8-2021
    def __str__(self): 
        return self.MeetingTitle

    class Meta: 
        db_table='Meeting' #tells what table name to use 
#end of first class 


#4. add meetingsMinutes class 4-8-2021
class MeetingMinutes(models.Model): 
    MeetingID = models.ForeignKey(Meeting, on_delete=models.CASCADE) #have to tell it where its relating to
    Attendance = models.ManyToManyField(User)
    MinuetesText = models.TextField(null=True, blank=True)

    #added the string method and class minutes 
    def __str__(self): 
        return str(self.MeetingID)

    class Meta: 
        db_table='Minutes' 
#end of second class 

#5 add Resources class 4-8-2021
class Resources(models.Model): 
    ResourceName = models.CharField(max_length=255) 
    ResourceType = models.CharField(max_length=255)  
    ResourceURL = models.URLField() 
    ResourceDate = models.DateField() 
    UserID = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    ResourceDescription = models.TextField(null=True, blank=True) 

    def __str__(self): 
        return self.ResourceName

    class Meta: 
        db_table='Resources' 
#end of third class 


#6 add events class 4-8-2021 
class Event(models.Model): 
    EventTitle = models.CharField(max_length=255) 
    EventLocation = models.CharField(max_length=255) 
    EventDate = models.DateField() 
    EventTime = models.TimeField() 
    EventDescription = models.TextField(null=True, blank=True) 
    UserID = models.ForeignKey(User, on_delete=models.DO_NOTHING) 

    #create string method and class Event 
    def __str__(self): 
        return self.EventTitle 

    class Meta: 
        db_table='Event' 
    

