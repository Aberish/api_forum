from django.forms import widgets
from rest_framework import serializers
from forum.models import *
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        owner = serializers.ReadOnlyField(source='owner.username')
        model = Comment
        fields = ('id', 'content', 'created', 'user', 'message')

class MessageSerializer(serializers.ModelSerializer):
    comments=CommentSerializer(many=True)
    class Meta:
        model = Message
        fields = ('id', 'title', 'content', 'created', 'updated', 'user', 'topic', 'comments')

class UserProfileOnlySerializer(serializers.ModelSerializer):
    class Meta:
        owner = serializers.ReadOnlyField(source='owner.username')
        model = UserProfile
        fields = ('id', 'username')


class UserProfileSerializer(serializers.ModelSerializer):
    topic_set = serializers.StringRelatedField(many=True)
    class Meta:
        owner = serializers.ReadOnlyField(source='owner.username')
        model = UserProfile
        fields = ('id', 'username','email', 'first_name', 'last_name', 'password', 'age', 'profile_picture', 'topic_set')

class TopicSerializer(serializers.ModelSerializer):
    messages = MessageSerializer(many=True)
    creator = UserProfileOnlySerializer(many=False)
    class Meta:
        owner = serializers.ReadOnlyField(source='owner.username')
        model = Topic
        fields = ('id', 'title', 'description', 'created', 'updated', 'imageURL','views', 'creator', 'messages', 'category', 'type_topic', 'favorite_topics')

class TopicFilterSerializer(serializers.ModelSerializer):
    creator = UserProfileOnlySerializer(many=False)
    class Meta:
        owner = serializers.ReadOnlyField(source='owner.username')
        model = Topic
        fields = ('id', 'title', 'description', 'created', 'updated', 'imageURL','views', 'creator')

class CategorySerializer(serializers.ModelSerializer):
    topics = TopicFilterSerializer(many=True)
    class Meta:
        owner = serializers.ReadOnlyField(source='owner.username')
        model = Category
        fields = ('id', 'name', 'slug', 'topics')



class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        owner = serializers.ReadOnlyField(source='owner.username')
        model = Type
        fields = ('id', 'name')