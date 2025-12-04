'''
BEFORE -->
blog_names = {
    "python-intro": "Python Post",
    "django-basics": "Django basics blog posts",
    "python-oops": "Object Oriented Programming Using Python",
    "regex": "Regular Expressions In Python",
    "tkinter": None
}
'''
''' AFTER -->
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
'''

'''
allposts.html file changes --> 
{% extends "base.html" %}
{% load static %}

{% block css_files %}
    <link rel="stylesheet" href="{% static 'blogs/app.css' %}"
{% endblock %}

{% block page_title %}
All Posts
{% endblock %}

{% block body_content %}
    <section>
        <h2>All My Posts</h2>
        <ul>
            {% for blog in blogs %}
                <li>
                    <article>
                        <a href="{% url 'blog-post' blog=blog.slug %}">{{ blog.title }}</a>
                        <img src="{% static 'blogs/images/' |add:blog.image %}" alt="{{ blog.title }}">
                        <div>
                            <p>{{ blog.preview }}}}</p>
                        </div>
                    </article>
                </li>
            {% endfor %}
        </ul>
    </section>

{% endblock %}
'''