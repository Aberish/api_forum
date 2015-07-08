from django.db import models

class UserProfile(models.Model):  
     username = models.CharField(max_length=20, blank=False, default='')
     email = models.EmailField()
     first_name = models.CharField(max_length=30)
     last_name = models.CharField(max_length=30)
     password = models.CharField(max_length=100)  
     age = models.IntegerField()
     profile_picture = models.ImageField(upload_to='assets/profil', blank=True)

class Category(models.Model):
    name = models.CharField(max_length=20, blank=False, default='')
    slug = models.CharField(max_length=20, blank=False, default='')

class Topic(models.Model):
    title = models.CharField(max_length=100, blank=True, default='')
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    imageURL = models.ImageField(upload_to='assets/topic', blank=True)
    vues = models.IntegerField(default=0)
    created_by = models.ForeignKey(UserProfile, related_name='topic')
    category = models.ForeignKey(Category, related_name='topic')
    def get_messages(self):
        messages = objects.filter(topicID=self)
        return messages

class Message(models.Model):
    title = models.CharField(max_length=100, blank=True, default='')
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    userID = models.ForeignKey(UserProfile, related_name='message_user')
    answerID = models.IntegerField(null=True, default=0)
    topicID = models.ForeignKey(Topic, related_name='message_topic')



class Comment(models.Model):
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    user_comment = models.ForeignKey(UserProfile, related_name='commentUser')
    answer_message = models.ForeignKey(Message, related_name='answer_message')