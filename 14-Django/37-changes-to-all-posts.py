'''
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
                        <a href="{% url 'blog-post' blog=blog %}">{{ blog|capfirst}}</a>
                        <img src="{% static 'blogs/images/simply.jpeg' %}" alt="Py">
                        <div>
                            <p>Python is a high level programming language.</p>
                        </div>
                    </article>
                </li>
            {% endfor %}
        </ul>
    </section>

{% endblock %}
'''