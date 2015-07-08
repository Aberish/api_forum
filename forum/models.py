from django.db import models

class UserProfile(models.Model):  
     username = models.CharField(max_length=20, blank=False, default='')
     email = models.EmailField()
     first_name = models.CharField(max_length=30)
     last_name = models.CharField(max_length=30)
     password = models.CharField(max_length=100)  
     age = models.IntegerField()
     profile_picture = models.ImageField(upload_to='thumbpath', blank=True)

class Message(models.Model):
    title = models.CharField(max_length=100, blank=True, default='')
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    userID = models.ForeignKey(UserProfile, related_name='message')
    answerID = models.IntegerField(null=True, default=0)
class Category(models.Model):
    name = models.CharField(max_length=20, blank=False, default='')

class Topic(models.Model):
    title = models.CharField(max_length=100, blank=True, default='')
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    imageURL = models.CharField(max_length=100, default='')
    vues = models.IntegerField()
    created_by = models.ForeignKey(UserProfile, related_name='topic')
    category = models.ForeignKey(Category, related_name='topic')
