# The urls are responsible for the website. We use URL for that website.
# There are internal routes or URLs. Whenever we click there will be particular page.
# So, myproject1.com is main url. This shows starting page.
# If you want.. myproject1.com/blogs..
# If you open any blog.. myproject1.com/blog/<particular blog>
# Each URL is mapped to a certain section.

# Views and URLs go hand-in-hand and work together. Views are actions, that gets triggered when you click URL.
# Views has main logic of our code.
# On a code level, view is a function, gets executed when a particular user clicks it.
# python manage.py runserver

# I defined this function in views.py file and then created another file named urls.py

# from django.http import HttpResponse
# def blogs(request):
#     return HttpResponse("My Blog List")

# In urls.py file,
# from django.urls import path
# from . import views
# urlpatterns = [
#     path("blogs", views.blogs)
# ]

# myproject1/urls.py
# path("app1/", include("app1.urls"))