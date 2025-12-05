# Created new file in helloworld, named serializers.py

# Serializers are used to translate django models to JSON format.
"""
In serializers.py -->
from rest_framework import serializers
from helloworld.models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__' # title, content, created_on ,updated_on are fields
"""

"""
In views.py --> 
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import APIView
from helloworld.serializers import PostSerializer
from rest_framework.viewsets import ModelViewSet
from helloworld.models import Post

# Create your views here.

class HelloWorldView(APIView):
    def get(self, request):
        return Response({'message': 'Hello World'})

class PostView(ModelViewSet): # INHERITANCE --> ModelViewSet --> MAKE A FULL CRUD API FOR POST MODEL
    queryset = Post.objects.all() # QUERYSET MEANS WHICH ROWS TO WORK WITH, LOAD ALL POSTS
    serializer_class = PostSerializer # SERIALIZER CLASS MEANS HOW TO CONVERT DATA.
"""

"""
urls.py inside blogs.
from django.contrib import admin
from django.urls import path
from helloworld.views import HelloWorldView
from rest_framework import routers
from helloworld.views import PostView

urlpatterns = [
    path("admin/", admin.site.urls),
    path('hello', HelloWorldView.as_view())
]

# WITHOUT ROUTER YOU WOULD MANUALLY WRITE URLs..
router = routers.SimpleRouter() # CREATING ROUTER OBJECT
router.register('post', PostView) # TELL ROUTER ABOUT VIEWSET
urlpatterns += router.urls # ADD AUTO-GENERATED URLs.
"""