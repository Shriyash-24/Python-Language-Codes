# In index.html -->
'''
{% extends "base.html" %}

{% block page_title %}
Blog Post Home Page
{% endblock %}

{% block body_content %}
    <h1>My Personal Blog Post</h1>
    <h2>I write about Python and related stuff.</h2>
{% endblock %}
'''

# posts.html before v/s after
'''
BEFORE -->
<!--This template is used for all posts, that's why we need to make HTML file dynamic-->

<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>{{ blog_namen}}</title>
</head>
<body>
    <h1>{{ blog_name|title }} Blog Post</h1>
    {% if blog_text %}
        <h2>{{ blog_text }}</h2>
    {% else %}
        <h2>"Blog is in progress...</h2>
    {% endif %}
</body>
</html>
'''

'''
AFTER --> 

{% extends "base.html" %}

{% block_page title %}
    {{ blog_name|title }}
{% endblock %}

{% block body_content %}
    <h1>{{ blog_name|title }} Blog Post</h1>
    {% if blog_text %}
        <h2>{{ blog_text }}</h2>
    {% else %}
        <h2>"Blog is in progress...</h2>
    {% endif %}
{% endblock %}
'''