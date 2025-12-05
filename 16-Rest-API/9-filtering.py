# Filtered based on usernames.
"""
views.py -->

from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import APIView
from helloworld.serializers import PostSerializer
from rest_framework.viewsets import ModelViewSet
from helloworld.models import Post
from rest_framework.permissions import IsAuthenticated
from helloworld.permissions import IsPostPossessor
from rest_framework import filters

# Create your views here.

class HelloWorldView(APIView):
    def get(self, request):
        return Response({'message': 'Hello World'})

class PostView(ModelViewSet):
    permission_classes = [IsAuthenticated, IsPostPossessor]
    serializer_class = PostSerializer
    filter_backends = [filters.SearchFilter]

def get_queryset(self):
    return Post.objects.filter(created_by = self.request.user) # “Return only posts that were created by the currently logged-in user.”
"""

"""
In urls.py --> 
from django.contrib import admin
from django.urls import path, include
from helloworld.views import HelloWorldView
from rest_framework import routers
from helloworld.views import PostView

urlpatterns = [
    path("admin/", admin.site.urls),
    path('hello', HelloWorldView.as_view()),
    path('api-auth/', include('rest_framework.urls')),
]

router = routers.SimpleRouter()
router.register('post', PostView, basename='post')
urlpatterns += router.urls
"""