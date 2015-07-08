from django.forms import widgets
from rest_framework import serializers
from forum.models import Message, UserProfile, Category, Topic

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        owner = serializers.ReadOnlyField(source='owner.username')
        model = Message
        fields = ('id', 'title', 'content', 'created', 'updated', 'userID', 'answerID')

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        owner = serializers.ReadOnlyField(source='owner.username')
        model = UserProfile
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'age', 'profile_picture')

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        owner = serializers.ReadOnlyField(source='owner.username')
        model = Category
        fields = ('id', 'name')

class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        owner = serializers.ReadOnlyField(source='owner.username')
        model = Topic
        fields = ('id', 'title', 'description', 'created', 'updated', 'imageURL','vues', 'created_by', 'category')
