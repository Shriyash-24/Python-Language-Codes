'''
def blog_post(request, blog):
    try:
        res = blog_names[blog]
        return render(request, "blogs/posts.html", {"blog_text":res})
    except Exception:
        return HttpResponseNotFound("<h1>Blog Not Found</h1>")
'''
# <h2>{{ blog_text }}</h2>