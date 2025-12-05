# Newly created file filters.py -->
"""
import django_filters
from django import forms
from helloworld.models import Post

class PostFilter(django_filters.FilterSet):
    created_on = django_filters.DateTimeFilter(widget = forms.DateInput(attrs={'type':'date'}), lookup_expr="date__exact")
    class Meta:
        model = Post
        fields = ['created_on']
"""

# views.py -->
"""
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import APIView
from helloworld.serializers import PostSerializer
from rest_framework.viewsets import ModelViewSet
from helloworld.models import Post
from rest_framework.permissions import IsAuthenticated
from helloworld.permissions import IsPostPossessor
from rest_framework import filters
from rest_framework import filters
from helloworld.filters import PostFilter
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.

class HelloWorldView(APIView):
    def get(self, request):
        return Response({'message': 'Hello World'})

class PostView(ModelViewSet):
    permission_classes = [IsAuthenticated, IsPostPossessor]
    serializer_class = PostSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filter_class = PostFilter
    search_fields = ['title', 'content']

def get_queryset(self):
    return Post.objects.filter(created_by = self.request.user)
"""