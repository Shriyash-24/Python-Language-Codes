# What else can we do with dynamic stuff.
# Path converter - Converts value entered in url which comes in path.

# urls.py
# path("allposts/<str:blog>", views.blog_post)

# Blog Posts by number.
# path("allposts/<int:blog>", views.blog_post_by_number)

# Sequence matters in urls.py, because otherwise it would convert 1 into string.

# views.py
def blog_post_by_number(request, blog):
    return HttpResponse(blog)