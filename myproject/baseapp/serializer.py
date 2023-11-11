from rest_framework import serializers
from .models import Topic

class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = ['text','date_added']

"""
class TopicSerializer(serializers.Serializer):
    
    class Meta:
        model = Topic
        fields = ['text','date_added']
"""
