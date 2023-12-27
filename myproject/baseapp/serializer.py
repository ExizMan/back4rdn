from rest_framework import serializers
from .models import Topic
import re
from django import forms
from .models import Employees, Professions




class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = ['text', 'date_added']




class EmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employees
        #fields = ['firstname', 'midname', 'lastname', 'profession']
        fields = '__all__'
    def validate(self, attrs):
        firstname = attrs.get('firstname','')
        midname = attrs.get('midname','')
        lastname = attrs.get('lastname','')
        if bool(re.search(r'[A-Za-z0-9,./<>?;:{}\[\]]', firstname)):
            raise serializers.ValidationError("Используйте только кириллицу")
        if bool(re.search(r'\s', firstname)):
            raise serializers.ValidationError("Пишите все в правильных полях")

        if midname is None:
            return None
        if bool(re.search(r'[A-Za-z0-9,./<>?;:{}\[\]]', midname)):
            raise serializers.ValidationError("Используйте только кириллицу")
        if bool(re.search(r'\s', midname)):
            raise serializers.ValidationError("Пишите все в правильных полях")

        if bool(re.search(r'[A-Za-z0-9,./<>?;:{}\[\]]', lastname)):
            raise serializers.ValidationError("Используйте только кириллицу")
        if bool(re.search(r'\s', lastname)):
            raise serializers.ValidationError("Пишите все в правильных полях")

        return attrs


class ProfessonsSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = Professions
        fields = ['id','tittle']
        #fields = '__all__'

    def validate(self,attrs):
        tittle = attrs.get('tittle','')
        if bool(re.search(r'[<>?;:{}\[\]]', tittle)):
            raise serializers.ValidationError("Вы используете какие-то подозрительные символы :/")
        return attrs





"""
class TopicSerializer(serializers.Serializer):
    def create(valid_data): 
    def update(v_data, instance):
    


        
"""
