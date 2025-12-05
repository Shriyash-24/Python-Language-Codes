# We created a new file named permissions.py
"""
from rest_framework import permissions

# permissions.BasePermission --> CUSTOM PERMISSION LOGIC
class IsPostPossessor(permissions.BasePermission):
    def has_object_permission(self, request, view, obj): # request --> HTTP request, view --> which view is being used, obj --> the post object
                        if request.method in permissions.SAFE_METHODS: (ONLY READ MODE)
                                    return True
                return obj.created_by == request.user
"""

# views.py file -->
"""
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import APIView
from helloworld.serializers import PostSerializer
from rest_framework.viewsets import ModelViewSet
from helloworld.models import Post
from rest_framework.permissions import IsAuthenticated
from helloworld.permissions import IsPostPossessor

class HelloWorldView(APIView):
    def get(self, request):
        return Response({'message': 'Hello World'})

class PostView(ModelViewSet):
    permission_classes = [IsAuthenticated, IsPostPossessor]
    ## BOTH MUST BE TRUE, IsAuthenticated. IsPostPossessor --> TRUE
    queryset = Post.objects.all() # Display all posts
    serializer_class = PostSerializer
"""