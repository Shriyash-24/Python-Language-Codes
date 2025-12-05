"""
views.py file under helloworld app -->
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import APIView

# Create your views here.

class HelloWorldView(APIView): # INHERITANCE --> Inheriting from API View
    def get(self, request):
        return Response({'message': 'Hello World'})
"""
"""
urls.py file under blogs -->
from django.contrib import admin
from django.urls import path
from helloworld.views import HelloWorldView
urlpatterns = [
    path("admin/", admin.site.urls),
    path('hello', HelloWorldView.as_view())
]
"""