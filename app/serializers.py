from rest_framework import serializers
from .models import User, Survey, Question, Response
from django.contrib.auth import get_user_model

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'name', 'email', 'password', 'role', 'created_at')
        extra_kwargs = {'password': {'write_only': True}}

    

    def validate_username(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email must be unique.")
        return value

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class SurveySerializer(serializers.ModelSerializer):
    class Meta:
        model = Survey
        fields = ('id', 'name', 'scheduled_date', 'scheduled_time', 'creator', 'target_users', 'invitations_send_flag', 'notification_send_flag', 'created_at', 'updated_at')

    def create(self, validated_data):
        user = Survey.objects.create(**validated_data)
        return user

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('id', 'questionlabel', 'survey_id', 'type', 'instructions', 'created_at')

    def create(self, validated_data):
        user = Question.objects.create(**validated_data)
        return user

class ResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Response
        fields = ('id', 'question_id', 'response', 'created_at', 'user_id')

    def create(self, validated_data):
        user = Response.objects.create(**validated_data)
        return user


        