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

# DICT WAY
'''
blog_names = {
    "python-intro": "<h1>Python Post</h1>",
    "django-basics": "<h1>Django basics blog posts</h1>",
    "python-oops": "<h1>Object Oriented Programming Using Python</h1>"

}

def blog_post(request, blog):
    try: 
        res = blog_names[blog]
    except Exception:
        return HttpResponseNotFound("<h1>Blog Not Found</h1>")
    else:
        return HttpResponse(res)
'''