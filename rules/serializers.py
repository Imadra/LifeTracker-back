from rest_framework import serializers
from .models import RuleTree

class RuleTreeSerializer(serializers.ModelSerializer):
    class Meta:
        model = RuleTree
        fields = '__all__'