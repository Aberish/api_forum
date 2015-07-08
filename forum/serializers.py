from django.forms import widgets
from rest_framework import serializers
from forum.models import *

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        owner = serializers.ReadOnlyField(source='owner.username')
        model = Message
        fields = ('id', 'title', 'content', 'created', 'updated', 'userID', 'answerID', 'topicID')

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        owner = serializers.ReadOnlyField(source='owner.username')
        model = UserProfile
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'age', 'profile_picture')

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        owner = serializers.ReadOnlyField(source='owner.username')
        model = Category
        fields = ('id', 'name', 'slug')

class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        owner = serializers.ReadOnlyField(source='owner.username')
        model = Topic
        messages = MessageSerializer(source='get_messsages', read_only=True)
        fields = ('id', 'title', 'description', 'created', 'updated', 'imageURL','vues', 'created_by', 'category', 'messages')

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        owner = serializers.ReadOnlyField(source='owner.username')
        model = Comment
        fields = ('id', 'content', 'created', 'user_comment', 'answer_message')
