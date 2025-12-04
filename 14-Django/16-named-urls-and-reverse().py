# Named URL - path("allposts/<slug:blog>", views.blog_post, name = "blog-post")

# So basically we try to replace 'allposts' to name to make it dynamic.

# We would want allposts
'''
def blogposts(request):
    return HttpResponse("<h1>Blogs Posts</h1>")
'''
# This approach is not dynamic as well.
'''
def blogposts(request):
    res_data = """
    <ul>
        <li><a href="allposts/python-intro">Python Intro</a></li>
        <li><a href="allposts/django-basics">Django Basics</a></li>
    </ul>
    """
    return HttpResponse(res_data)
'''
# Dynamic Approach
'''
def blogposts(request):
    list_items = ""
    blog_list = list(blog_names.keys())
    for b in blog_list:
        blog_path = reverse("blog-post", args=[b])
        list_items += f'<li><a href="{blog_path}">{b.capitalize()}</a></li>'
    res_data = f"<ul>{list_items}</ul>"
    return HttpResponse(res_data)
'''