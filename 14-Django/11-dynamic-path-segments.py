# If you want to have multiple blogs?
# We can add more view functions.

# Let's say we don't know.. how many blogs will be there.. it will be great if we can setup dynamically.

# path("allposts/<blog>", views.python_oops)

"""
def blog_post(request, blog):
    if blog == "python-intro":
        res = "Python Post"
    elif blog == "django-basics":
        res = "Django basics blog posts"
    elif blog == "python-oops":
        res = "Object Oriented Programming Using Python"
    else:
        return HttpResponseNotFound("Blog Not Found")

    return HttpResponse("")
"""