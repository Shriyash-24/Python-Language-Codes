"""
models.py file -->
class Post(models.Model): --> INHERITANCE --> Inheriting from models.Model --> Django creates a database table for this class
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

def __str__(self):
    return self.title
"""

# We run in terminal -->
# python manage.py makemigrations
# python manage.py migrate
# python manage.py createsuperuser
# We can login now in django administration panel
# In admin.py file -->
"""
from django.contrib import admin
from helloworld.models import Post

# Register your models here.
admin.site.register(Post)
"""
