'''
def process_blog_name(blog):
    blog_list = blog.split("-")
    return " ".join(blog_list).title()

def blog_post(request, blog):
    try:
        res = blog_names[blog]
        return render(request, "blogs/posts.html", {
            "blog_text":res, "blog_name": process_blog_name(blog)})
    except Exception:
        return HttpResponseNotFound("<h1>Blog Not Found</h1>")

'''