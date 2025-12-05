"""
models.py updation -->
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE) # EACH POST BELONGS TO USER,
    # USER IS FROM DJANGO'S BUILT-IN AUTH SYSTEM, FOREIGN KEY IS RELATION BETWEEN 2 TABLES,
    # on_delete=models.CASCADE --> USER DELETED --> ALL POST DELETE.

def __str__(self):
    return self.title
"""

"""
serailizers.py updation -->
from rest_framework import serializers
from helloworld.models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'# title, content, created_on ,updated_on are fields
        read_only_fields = ('created_by',) # CLIENT SHOULD NOT SEND CREATED_BY IN REQUEST DATA

def create(self, validated_data): # VALIDATED_DATA MEANS SAFE, VALIDATED I/P
    validated_data['created_by'] = self.context['request'].user
    return Post.objects.create(**validated_data)

"""