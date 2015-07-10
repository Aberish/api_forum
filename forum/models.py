from django.db import models


class UserProfile(models.Model):  
    username = models.CharField(unique=True,max_length=20, blank=False, default='')
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    password = models.CharField(max_length=100)  
    age = models.IntegerField()
    profile_picture = models.ImageField(upload_to='assets/profil', blank=True)
    def __unicode__(self):
        return u'%s %s' % (self.first_name, self.last_name)

class Category(models.Model):
    name = models.CharField(max_length=20, blank=False, default='')
    slug = models.SlugField(max_length=20, blank=False, default='')
    def __unicode__(self):
        return u'%s' % (self.name)

class Type(models.Model):
    name = models.CharField(max_length=30) 
    def __unicode__(self):
        return u'%s' % (self.name)

class Topic(models.Model):
    title = models.CharField(max_length=100, blank=True, default='')
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    imageURL = models.ImageField(upload_to='assets/topic', blank=True)
    views = models.IntegerField(default=0)
    creator = models.ForeignKey(UserProfile, related_name='topics')
    category = models.ForeignKey(Category, related_name='topics')
    type_topic = models.ForeignKey(Type, related_name='topics')
    favorite_topics = models.ManyToManyField(UserProfile, blank=True)
    def __unicode__(self):
        return u'%s' % (self.title)

class Message(models.Model):
    title = models.CharField(max_length=100, blank=True, default='')
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(UserProfile, related_name='messages')
    topic = models.ForeignKey(Topic, related_name='messages')
    favorite_message = models.ManyToManyField(UserProfile, blank=True)
    def __unicode__(self):
        return u'%s' % (self.title)

class Comment(models.Model):
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(UserProfile, related_name='comments')
    message = models.ForeignKey(Message, related_name='comments')
    def __unicode__(self):
        return u'%s' % (self.content)
