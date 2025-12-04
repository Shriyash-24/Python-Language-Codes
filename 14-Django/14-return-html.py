''' BEFORE -->
def blog_post(request, blog):
    if blog == "python-intro":
        res = "Python Post"
    elif blog == "django-basics":
        res = "Django basics blog posts"
    elif blog == "python-oops":
        res = "Object Oriented Programming Using Python"
    else:
        return HttpResponseNotFound("Blog Not Found")
    return HttpResponse(res)
'''

'''
def blog_post(request, blog):
    if blog == "python-intro":
        res = "<h1>Python Post</h1>"
    elif blog == "django-basics":
        res = "<h1>Django basics blog posts</h1>"
    elif blog == "python-oops":
        res = "<h1>Object Oriented Programming Using Python</h1>"
    else:
        return HttpResponseNotFound("<h1>Blog Not Found</h1>")
    return HttpResponse(res)
'''

# In real world projects, we have full HTML code. Right now, this is good start.