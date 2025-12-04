'''
def blog_post(request, blog):
    try:
        res = blog_names[blog]
        return render(request, "blogs/posts.html", {
            "blog_text":res, "blog_name": process_blog_name(blog)})
    except Exception:
        return HttpResponseNotFound("<h1>Blog Not Found</h1>")
'''

# Here we are still using Blog not found, hard coded values.
# 404.html should be the name.
# It acts a website for errors.
## render function also give success responses.
## So we have to use render_to_string

# One way
'''
def blog_post(request, blog):
    try:
        res = blog_names[blog]
        return render(request, "blogs/posts.html", {
            "blog_text":res, "blog_name": process_blog_name(blog)})
    except Exception:
        res_data = render_to_string("404.html")
        return HttpResponseNotFound(res_data)
'''

'''
def blog_post(request, blog):
    try:
        res = blog_names[blog]
        return render(request, "blogs/posts.html", {
            "blog_text":res, "blog_name": process_blog_name(blog)})
    except Exception:
        raise Http404() 
'''
# We haven't given 404.html because django will automatically get it.
# We have to set DEBUG = False when we deploy the website in the production.
