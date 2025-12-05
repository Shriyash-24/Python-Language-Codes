"""
Made changes in views.py file -->

from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import APIView
from helloworld.serializers import PostSerializer
from rest_framework.viewsets import ModelViewSet
from helloworld.models import Post
from rest_framework.permissisons import IsAuthenticated # IMPORTS PERMISSION CLASS

# Create your views here.

class HelloWorldView(APIView):
    def get(self, request):
        return Response({'message': 'Hello World'})

class PostView(ModelViewSet):
    permission_classes = [IsAuthenticated] # ONLY AUTHENITICALED LOGGED IN USERS CAN USE THIS API
    queryset = Post.objects.all() # Display all posts
    serializer_class = PostSerializer
"""

# from rest_framework.permissisons import IsAuthenticated
# permission_classes = [IsAuthenticated]

# Made changes in urls.py --> path('api-auth/', include('rest_framework.urls')),
# This line enables login/logout pages for DRF.