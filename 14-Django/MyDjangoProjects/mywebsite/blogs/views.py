from datetime import date
from django.shortcuts import render
from django.http import Http404, HttpResponse, HttpResponseNotFound
from django.urls import reverse
from django.template.loader import render_to_string

blog_details = [
    {
        "slug": "python-intro",
        "image": "simply.jpeg",
        "date": date(2025,10,15),
        "title": "Python Introduction",
        "preview": """Python is an open source, high level programming language that is used widely. 
        Application of Python are software development, data science, AI/ML etc..""",
        "content": """Python is brilliant language. This should be a huge paragraph."""
    },
    {
        "slug": "django-basics",
        "image": "simply.jpeg",
        "date": date(2025,10,20),
        "title": "Django Basics",
        "preview": """The Django Framework is a free, open-source framework. Should be longer..""",
        "content": """Write longer text here."""
    },
    {
        "slug": "python-oops",
        "image": "simply.jpeg",
        "date": date(2025, 10, 30),
        "title": "Python OOPs",
        "preview": """The Python oops is brilliant feature. Should be longer..""",
        "content": """Write longer text here."""
    },
    {
        "slug": "regex",
        "image": "simply.jpeg",
        "date": date(2025, 10, 300),
        "title": "Regex",
        "preview": """Regular Framework""",
        "content": """Write longer text here."""
    }

]
# Create your views here.
def home_page(request):
    sorted_blogs = sorted(blog_details, key=lambda post:post['date'], reverse=True)
    latest_blogs = sorted_blogs[:2]
    return render(request, "blogs/index.html", {"l_blogs": latest_blogs})

def blogposts(request):
    return render(request, "blogs/allposts.html", {"blogs": blog_details})
    for b in blog_list:
        blog_path = reverse("blog-post", args=[b])
        list_items += f'<li><a href="{blog_path}">{b.capitalize()}</a></li>'
    res_data = f"<ul>{list_items}</ul>"
    return HttpResponse(res_data)

def process_blog_name(blog):
    blog_list = blog.split("-")
    return " ".join(blog_list).title()

def blog_post(request, blog):
    try:
        res = blog_names[blog]
        return render(request, "blogs/posts.html", {
            "blog_text":res, "blog_name": process_blog_name(blog)})
    except Exception:
        raise Http404()



