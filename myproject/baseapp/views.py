from django.shortcuts import render
from .models import Topic

from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import TopicSerializer

class TopicView(APIView):
    def get(self,request):
        output=[
            {
                "text":output.text,

            } for output in Topic.objects.all()
        ]
        return Response(output)
    def post(self,request):
        serializer = TopicSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
# Create your views here.
