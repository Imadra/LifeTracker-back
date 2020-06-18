from rest_framework import serializers
from .models import Task, Day

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

class DaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Day
        fields = '__all__'