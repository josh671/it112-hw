from django.db import models
from django.test import TestCase
from django.contrib.auth.models import User
from .models import Meeting, MeetingMinutes, Resources, Event
from datetime import datetime
from django.urls import reverse
from django.contrib.auth.models import User 


# Create your tests here.
#This works and shows 2 test with 2 OK's but only when I remove MeetingMinutesTest
class MeetingTest(TestCase): 
    def setUp(self): 
        self.type=Meeting(MeetingTitle='Soccer Meeting')
    

    def test_typestring(self): 
        self.assertEqual(str(self.type), 'Soccer Meeting')
    
    def test_tablename(self): 
        self.assertEqual(str(Meeting._meta.db_table), 'Meeting')

#This does not work and I don't know why. 
#I think it has something to do with Attendance being aa manytomanyfield(user)
class MeetingMinutesTest(TestCase): 
   def setUp(self):
       self.type=Meeting(MeetingTitle='1')
       self.user=User(username='josh') 

       self.Mins = MeetingMinutes(MeetingID=self.type, Attendance=MeetingMinutes.set(self.user),  MinuetesText="blah")
   def test_string(self): 
        self.assertEqual(str(self.Mins), '1')

   def test_tablename(self): 
        self.assertEqual(str(MeetingMinutes._meta.db_table), 'Minutes')

class ResourcesTest(TestCase): 
    def setUp(self): 
        self.type=Resources(ResourceName='w3schools') 
        self.user=User(username='josh')
        self.resources=Resources(ResourceName='comics', ResourceType=self.type, ResourceURL="w3schools.com", ResourceDate='1/10/2021', UserID=self.user, ResourceDescription="Learning site"  ) 

    def test_string(self): 
        self.assertEqual(str(self.resources), 'comics') 

    def test_tablename(self): 
        self.assertEqual(str(Resources._meta.db_table), 'Resources') 

class EventTest(TestCase): 
    def setUp(self): 
        self.type=Event(EventTitle='Soccer Event'); 
        self.user = User(username='josh'); 
        self.events=Event(EventTitle='Sports Event', EventLocation="Hagatna",  EventDate='1/10/2021', EventTime="15:00", EventDescription="Learning site", UserID=self.user,  )

    def test_string(self): 
        self.assertEqual(str(self.events), 'Sports Event') 

    def test_tablename(self): 
        self.assertEqual(str(Event._meta.db_table), 'Event') 