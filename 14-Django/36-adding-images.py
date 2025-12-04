'''
{% extends "base.html" %}
{% load static %}

{% block css_files %}
    <link rel="stylesheet" href="{% static 'blogs/app.css' %}"
{% endblock %}

{% block page_title %}
Blog Post Home Page
{% endblock %}

{% block body_content %}
    <header>
        <h1><a href="">Home Page</a></h1>
        <nav>
            <a href="">All Posts</a>
        </nav>
    </header>
    <section>
        <header>
            <h1>My Personal Blog Post</h1>
            <h2>I write about Python and related stuff.</h2>
            <img src="{% static 'blogs/images/simply.jpeg' %}" alt="Home Image"/>
        </header>
    </section>

    <section>
        <h2>Featured Posts</h2>
        <ul>
            <li>
                <article>
                    <a href="">
                        <img src="{% static 'blogs/images/simply.jpeg' %}" alt="Python" />
                        <div>
                            <h3>Python Intro</h3>
                            <p>Python is a high level programming language.</p>
                        </div>
                    </a>
                </article>
            </li>
            <li>
                <article>
                    <a href="">
                        <img src="{% static 'blogs/images/simply.jpeg' %}" alt="Django" />
                        <div>
                            <h3>Django Basics</h3>
                            <p>Django Basics</p>
                        </div>
                    </a>
                </article>
            </li>

        </ul>
    </section>
    <section>
        <h2>About the Author</h2>
        <p>The Author has 10+ years of experience in software and app development.
        He also makes content on Python and Django.
        </p>
        <p>
            Contact the author on contact@example.con
        </p>
    </section>


{% endblock %}
'''